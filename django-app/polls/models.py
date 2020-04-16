from django.db import models
from django.utils import timezone
import datetime



class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_eans = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.vendor_name


