from django.db import models

class Merchant(models.Model):
    merchant_name = models.CharField(max_length=250)
    merchant_code = models.CharField(max_length=25)
    merchant_address = models.TextField()

