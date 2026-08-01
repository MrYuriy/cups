from django.http import FileResponse, Http404, HttpResponseNotModified

from .models import DeviceType, Firmware


def firmware_download(request, device_type):
    """
    Віддає активну прошивку для типу пристрою (label / stock) для OTA.

    ESP (Arduino HTTPUpdate) шле свою поточну версію в хедері `x-ESP32-version`:
    - версія збігається з активною → 304 Not Modified (нічого не качаємо);
    - активної прошивки ще немає → теж 304 (оновлювати нема на що, щоб ESP не
      логував OTA FAILED);
    - інакше → 200 з тілом .bin (стрімиться з диска).
    """
    if device_type not in DeviceType.values:
        raise Http404("Unknown device type")

    fw = (
        Firmware.objects.filter(device_type=device_type, is_active=True)
        .first()
    )
    if not fw:
        return HttpResponseNotModified()

    current = request.headers.get("x-ESP32-version", "")
    if current and current == fw.version:
        return HttpResponseNotModified()

    try:
        handle = fw.file.open("rb")
    except FileNotFoundError:
        # Запис у БД є, а файлу на диску нема (напр. загубився при ребілді без volume)
        raise Http404("Firmware file missing")

    filename = fw.file.name.rsplit("/", 1)[-1]
    response = FileResponse(handle, content_type="application/octet-stream")
    response["X-Firmware-Version"] = fw.version
    response["X-Firmware-SHA256"] = fw.sha256
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
