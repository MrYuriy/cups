import urequests

import network
ssid = "wi-fi_name"
password = "wi-fi"

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)  # Connect to the WiFi network

        while not wlan.isconnected():  # Wait until connected
            pass

connect_to_wifi()
