from django.contrib import admin
from .models import Label, LabelStock


class LabelAdmin(admin.ModelAdmin):
    list_display = ("identifier", "print_status", "order", "shop", "data")
    search_fields = ("identifier",)
    list_filter = ("print_status", "shop",)


class LabelStockAdmin(admin.ModelAdmin):
    list_display = ("identifier", "print_status", "pre_advice", "data")
    search_fields = ("identifier",)
    list_filter = ("print_status",)


admin.site.register(Label, LabelAdmin)
admin.site.register(LabelStock, LabelStockAdmin)
