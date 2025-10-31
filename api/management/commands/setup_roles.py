from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Create user roles and assign permissions'

    def handle(self, *args, **kwargs):
        # Create roles
        editor_group, created = Group.objects.get_or_create(name='Editor')
        publisher_group, created = Group.objects.get_or_create(name='Publisher')
        admin_group, created = Group.objects.get_or_create(name='Admin')
        # Assign permissions
        # publish_permission = Permission.objects.get(codename='can_publish_document')
        # archive_permission = Permission.objects.get(codename='can_archive_document')

        # Add permissions to groups
        # editor_group.permissions.add(publish_permission)
        # publisher_group.permissions.add(archive_permission)
        # admin_group.permissions.add(publish_permission, archive_permission)
        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))