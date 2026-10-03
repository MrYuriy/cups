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


class ReturnLabel(models.Model):
    """Pieces of one returned order, printed 10x10 cm: one record per kind of goods.

    lines_info is a list of {"reference": str, "quantity": int}; it is split across as many
    labels as it needs, numbered 1/3, 2/3, 3/3 within this record.
    """

    INTACT = "intact"
    DAMAGED = "damaged"
    KINDS = [(INTACT, "pelnowartosciowe"), (DAMAGED, "uszkodzone")]

    data = models.CharField(max_length=10, default="", null=True, blank=True)
    oh_number = models.CharField(max_length=20, default="", null=True, blank=True)
    kind = models.CharField(max_length=10, choices=KINDS, default=INTACT)
    lines_info = models.JSONField(null=True, blank=True)
    print_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Etykieta zwrotu"
        verbose_name_plural = "Etykiety zwrotów"

    def __str__(self):
        return f"{self.oh_number} {self.kind}"


class LabelStock(models.Model):
    supplier_company = models.CharField(max_length=100)
    user = models.CharField(max_length=50, default="", null=True, blank=True)
    data = models.CharField(max_length=10, default="", null=True, blank=True)
    pre_advice = models.CharField(max_length=12, default="", null=True, blank=True)
    master_id = models.CharField(max_length=15, default="", null=True, blank=True)
    identifier = models.CharField(max_length=12, default="", null=True, blank=True)
    delivery_part = models.CharField(max_length=12, default="", null=True, blank=True)
    print_status = models.BooleanField(default=False)
    lines_info = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.identifier
    
    