from django.db import models

class ProviderInvoice(models.Model):
    invoice_date = models.DateTimeField()
    invoice_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
