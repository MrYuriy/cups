from django.contrib import admin
from .models import Label, LabelStock, ReturnLabel


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


@admin.register(ReturnLabel)
class ReturnLabelAdmin(admin.ModelAdmin):
    """Etykiety zwrotów e-com: po jednym wpisie na rodzaj towaru (całe / uszkodzone)."""

    list_display = ("oh_number", "data", "kind", "positions", "pieces", "print_status", "created_at")
    search_fields = ("oh_number",)
    list_filter = ("print_status", "kind", "data")
    ordering = ("-created_at",)
    actions = ("print_again",)

    @admin.display(description="Pozycji")
    def positions(self, obj):
        return len(obj.lines_info or [])

    @admin.display(description="Sztuk")
    def pieces(self, obj):
        return sum(line.get("quantity", 0) for line in (obj.lines_info or []))

    @admin.action(description="Wydrukuj ponownie")
    def print_again(self, request, queryset):
        # The ESP takes whatever is not printed yet, so clearing the flag queues it again.
        updated = queryset.update(print_status=False)
        self.message_user(request, f"Do druku: {updated}")


admin.site.register(Label, LabelAdmin)
# admin.site.register(LabelStock, LabelStockAdmin)
