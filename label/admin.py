from django.contrib import admin
from .models import Label


class LabelAdmin(admin.ModelAdmin):
    list_display = ("identifier", "print_status", "order", "shop", "data")
    search_fields = ("identifier",)
    list_filter = ("print_status", "shop",)


admin.site.register(Label, LabelAdmin)
