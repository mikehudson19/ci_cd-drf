import logging
import django_rq
from django_rq.management.commands import rqscheduler
from jobs import funct_store as funct
from jobs.models import ScheduledJob

scheduler = django_rq.get_scheduler()
log = logging.getLogger(__name__)

def clear_scheduled_jobs():
    # Delete any existing jobs in the scheduler when the app starts up
    for job in scheduler.get_jobs():
        log.debug("Deleting scheduled job %s", job)
        job.delete()

def register_scheduled_jobs():
    """
        Add jobs to the Redis queue.
        Only add active jobs.
    """

    jobs = [
        { 'args': None, 'funct': 'pull_customer_data', 'cron': '* * * * *', 'result_ttl': 3600, 'ttl': 3600, 'queue': 'default'},
        { 'args': None, 'funct': 'pull_billing_line_data', 'cron': '* * * * *', 'result_ttl': 3600, 'ttl': 3600, 'queue': 'default'}
    ]

    for j in jobs:
        args = j['args'] or []
        scheduler.cron(
            j['cron'],
            func=getattr(funct, j['funct']),
            args=args,
            repeat=None,
            result_ttl=j['result_ttl'],
            ttl=j['ttl'],
            use_local_timezone=False,
            queue_name=j['queue']
        )

class Command(rqscheduler.Command):
    def handle(self, *args, **kwargs):
        # This is necessary to prevent dupes
        clear_scheduled_jobs()

        register_scheduled_jobs()
        super(Command, self).handle(*args, **kwargs)

