"""Допоміжні функції для роботи з активною прошивкою."""
from .models import Firmware, DeviceType


def get_active_version(device_type: str) -> str | None:
    """
    Версія активної прошивки для типу пристрою (один індексований запит).

    Використовується для хедера X-Firmware-Version на ендпоінтах, які опитує
    ESP. Читаємо з БД щоразу навмисно: gunicorn працює в кількох воркерах, тож
    in-memory кеш був би неузгодженим і віддавав би застарілу версію. Запит —
    одна маленька стрічка по індексу (device_type, is_active), це дешево, зате
    хедер оновлюється миттєво щойно адмін залив нову прошивку.
    """
    if device_type not in DeviceType.values:
        return None
    return (
        Firmware.objects.filter(device_type=device_type, is_active=True)
        .values_list("version", flat=True)
        .first()
    )
