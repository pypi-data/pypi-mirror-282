import json
from pathlib import Path
from typing import Any

import structlog
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db import transaction

from payla_utils.settings import payla_utils_settings

logger = structlog.get_logger(__name__)


class Command(BaseCommand):
    """
    Django management command to set up user groups and permissions based on a JSON configuration file.

    This command performs two main functions:
        1. Adding Permissions: it reads a JSON file that defines groups and their respective permissions.
           For each group, the command creates it in the database (if it doesn't already exist) and assigns
           the specified permissions to it.
        2. Removing Unspecified Permissions: the command also checks for and removes any permissions
           currently assigned to the group but not specified in the JSON configuration. This ensures that
           each group only has the permissions explicitly defined in the configuration.

    Example JSON structure:
    {
        "core": {
            "bank": {
                "view_bank": [
                    {"group": "customer_service_level_1", "envs": ["playground", "prod", "stage", "dev"]},
                ],
                "change_bank": [
                    {"group": "finance", "envs": ["prod", "stage"]},
                ]
            }
        }
    }

    Where core is the app_label, bank is the model name, view_bank is the permission codename
    """

    help = 'Syncs user groups and permissions based on a JSON configuration file.'

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> str | None:
        current_env = 'dev' if settings.ENVIRONMENT == 'local.dev' else settings.ENVIRONMENT

        # check if the file exists
        if not payla_utils_settings.GROUPS_PERMISSIONS_FILE_PATH:
            logger.warning("Skipping sync_groups command. No GROUPS_PERMISSIONS_FILE_PATH defined in settings.")
            return None

        with Path.open(payla_utils_settings.GROUPS_PERMISSIONS_FILE_PATH, encoding='utf-8') as f:
            group_definition = json.loads(f.read())

        groups_permissions = self.assign_permissions(group_definition, current_env)

        self.remove_unused_permissions(groups_permissions)

        return None

    def assign_permissions(
        self,
        group_definition: dict,
        current_env: str,
    ) -> dict[str, list[str]]:
        groups_permissions: dict[str, list[str]] = {}
        for app_label, app_data in group_definition.items():
            for model_name, model_data in app_data.items():
                for permission_codename, permission_data in model_data.items():
                    permission_code = f"{permission_codename}.{app_label}.{model_name}"

                    try:
                        permission = Permission.objects.get_by_natural_key(permission_codename, app_label, model_name)
                    except Permission.DoesNotExist:
                        logger.exception("Permission %s not found!", permission_code)
                        continue

                    for permission_group in permission_data:
                        envs = permission_group.get('envs', [])
                        group_name = permission_group['group']

                        if current_env not in envs:
                            logger.info(
                                "Skipping permission %s for group %s in environment %s",
                                permission_codename,
                                group_name,
                                current_env,
                            )
                            continue

                        # Create group
                        group = Group.objects.get_or_create(name=group_name)[0]

                        groups_permissions.setdefault(group_name, [])

                        # Add permission to group
                        group.permissions.add(permission)
                        logger.info("Added permission %s to group %s", permission_codename, group_name)
                        groups_permissions[group_name].append(permission_codename)
        return groups_permissions

    def remove_unused_permissions(self, groups_permissions: dict[str, list[str]]) -> None:
        # Remove unused permissions from group
        for group_name, permissions in groups_permissions.items():
            group = Group.objects.get(name=group_name)
            removed_permissions = 0
            for permission in group.permissions.all():
                if permission.codename not in permissions:
                    logger.info("Removing permission %s from group %s", permission.codename, group_name)
                    group.permissions.remove(permission)
                    removed_permissions += 1
            logger.info("Removed %s permissions from group %s", removed_permissions, group_name)
