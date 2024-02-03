from django.db import models

class Label(models.Model):
    supplier_company = models.CharField(max_length=100)
    shop = models.CharField(max_length=3)
    user = models.CharField(max_length=50)
    data = models.CharField(max_length=10)
    order = models.CharField(max_length=8)
    identifier = models.CharField(max_length=12)
    print_status = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier
    
    