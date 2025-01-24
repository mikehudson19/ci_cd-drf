from django.db import models

class ScheduledJob(models.Model):
    JOB_TYPE_CHOICES = [
        ('PULL', 'Pull'),
        ('PUSH', 'Push'),
        ('VALIDATE', 'Validate'),
    ]

    cron = models.CharField(max_length=100)
    funct = models.CharField(max_length=255)
    args = models.CharField(max_length=255, null=True)
    kwargs = models.CharField(max_length=255, null=True)
    repeat = models.IntegerField(null=True)
    result_ttl = models.IntegerField(null=True)
    ttl = models.IntegerField(null=True)
    queue = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.id