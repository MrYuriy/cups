from django.db import models

class Label(models.Model):
    supplier_company = models.CharField(max_length=100)
    shop = models.CharField(max_length=3, default="", null=True, blank=True)
    user = models.CharField(max_length=50, default="", null=True, blank=True)
    data = models.CharField(max_length=10, default="", null=True, blank=True)
    order = models.CharField(max_length=8, default="", null=True, blank=True)
    identifier = models.CharField(max_length=12, default="", null=True, blank=True)
    comment = models.CharField(max_length=100, default="", null=True, blank=True)
    print_status = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier
    
    