from django.contrib import admin
from .models import Label, LabelStock


class LabelAdmin(admin.ModelAdmin):
    list_display = ("identifier", "print_status", "order", "shop", "data")
    search_fields = ("identifier",)
    list_filter = ("print_status", "shop",)


@admin.register(LabelStock)
class LabelStockAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "supplier_company", 
        "user", 
        "identifier", 
        "print_status", 
        "lines_info"
    )  # Поля для відображення
    search_fields = ("supplier_company", "identifier", "user")  # Поля для пошуку
    list_filter = ("print_status",)  # Фільтри для зручності
    ordering = ("supplier_company",)  # Сортування за замовчуванням
    list_editable = ("print_status",)  # Можливість редагування статусу прямо у списку
    #readonly_fields = ("lines_info",)  # Поле тільки для читання (не можна редагувати через адмінку)

    # Опціонально, якщо потрібно візуалізувати поле JSON у більш читабельному вигляді
    def pretty_lines_info(self, obj):
        import json
        return json.dumps(obj.lines_info, indent=4)  # Красивий формат JSON
    pretty_lines_info.short_description = "Lines Info (Formatted)"

admin.site.register(Label, LabelAdmin)
# admin.site.register(LabelStock, LabelStockAdmin)
