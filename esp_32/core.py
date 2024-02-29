import machine
import time
from wi_fi_connect import connect_to_wifi
from print_label import print_label, get_label_code

# Ініціалізуємо таймер спостереження з таймаутом 60 секунд
wdt = machine.WDT(timeout=60000)
endpoint_url = "your_endpoint_url_to_cups_get_method"
def main():
    connect_to_wifi()
    while True:
        try:
            label_code = get_label_code(endpoint_url)
            if label_code:
                print_label(label_code)
            # Живимо таймер спостереження, щоб уникнути скидання пристрою
            wdt.feed()
        except Exception as e:
            print("Exception:", e)
            connect_to_wifi()
            # Якщо виникла помилка, знову підключаємося до Wi-Fi і спробуємо отримати та роздрукувати мітку
            try:
                label_code = get_label_code(endpoint_url)
                if label_code:
                    print_label(label_code)
            except Exception as e:
                print("Retry failed:", e)

        
main()

