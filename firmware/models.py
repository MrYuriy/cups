import hashlib

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

# Прошивки лежать на диску (FIRMWARE_ROOT), не в публічній media —
# віддаються тільки через download-view (стрімом). У БД — лише метадані.
firmware_storage = FileSystemStorage(location=str(settings.FIRMWARE_ROOT))


class DeviceType(models.TextChoices):
    LABEL = "label", "Label"
    STOCK = "stock", "Stock"


def firmware_upload_to(instance, filename):
    # Розкладаємо по підпапках за типом пристрою
    return f"{instance.device_type}/{filename}"


class Firmware(models.Model):
    """
    Прошивка ESP для одного з двох типів пристроїв (label / stock).
    Активна — та, у якої is_active=True (одночасно тільки одна на тип).
    Формат файлу — .bin, як у проєкті Pinokio.
    """
    device_type = models.CharField(max_length=16, choices=DeviceType.choices)
    version = models.CharField(max_length=64)
    file = models.FileField(upload_to=firmware_upload_to, storage=firmware_storage)

    size = models.PositiveIntegerField(default=0, editable=False)
    sha256 = models.CharField(max_length=64, blank=True, editable=False)

    is_active = models.BooleanField(default=True)
    uploaded_by = models.CharField(max_length=150, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
        indexes = [
            models.Index(fields=["device_type", "is_active"]),
        ]

    def __str__(self):
        return f"{self.get_device_type_display()} v{self.version}"

    def save(self, *args, **kwargs):
        # Порахувати розмір і sha256 з файлу при заливці
        if self.file and not self.sha256:
            self.file.open("rb")
            content = self.file.read()
            self.size = len(content)
            self.sha256 = hashlib.sha256(content).hexdigest()
            self.file.seek(0)

        super().save(*args, **kwargs)

        # Гарантувати єдину активну прошивку на тип пристрою
        if self.is_active:
            Firmware.objects.filter(
                device_type=self.device_type, is_active=True
            ).exclude(pk=self.pk).update(is_active=False)


# ---- Proxy-моделі → два окремі пункти в Django-admin ----

class LabelFirmware(Firmware):
    class Meta:
        proxy = True
        verbose_name = "Label firmware"
        verbose_name_plural = "Label firmware"


class StockFirmware(Firmware):
    class Meta:
        proxy = True
        verbose_name = "Stock firmware"
        verbose_name_plural = "Stock firmware"
