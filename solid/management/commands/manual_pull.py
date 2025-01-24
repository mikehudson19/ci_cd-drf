from django.core.management.base import BaseCommand, CommandError

from solid.scheduled_pull.tasks import pull_customer_data, pull_billing_line_data


class Command(BaseCommand):
    help = 'Testing second command'

    def handle(self, *args, **options):
        pull_customer_data()
        pull_billing_line_data()

