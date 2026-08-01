from django.contrib import admin

from .models import DeviceType, LabelFirmware, StockFirmware


class BaseFirmwareAdmin(admin.ModelAdmin):
    """
    Спільна логіка для двох типів прошивок. Кожен нащадок прив'язаний до свого
    device_type, тож в адмінці це два окремі пункти («Label firmware» /
    «Stock firmware»), кожен зі своєю формою заливки файлу.
    """
    device_type = None

    list_display = ("version", "file", "size", "is_active", "uploaded_at", "uploaded_by")
    list_filter = ("is_active",)
    readonly_fields = ("size", "sha256", "uploaded_by", "uploaded_at")
    fields = ("version", "file", "is_active", "size", "sha256", "uploaded_by", "uploaded_at")

    def get_queryset(self, request):
        return super().get_queryset(request).filter(device_type=self.device_type)

    def save_model(self, request, obj, form, change):
        # device_type виставляємо самі — його немає у формі
        obj.device_type = self.device_type
        if not obj.uploaded_by:
            obj.uploaded_by = request.user.get_username()
        super().save_model(request, obj, form, change)


@admin.register(LabelFirmware)
class LabelFirmwareAdmin(BaseFirmwareAdmin):
    device_type = DeviceType.LABEL


@admin.register(StockFirmware)
class StockFirmwareAdmin(BaseFirmwareAdmin):
    device_type = DeviceType.STOCK
