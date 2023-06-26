# Ejemplo N°18: Conectar la RPico W a una red WiFi

import network
from utime import sleep

ssid = 'CAMBIA POR TU SSID'
password = 'TU PASSWORD'

red = network.WLAN(network.STA_IF)

red.active(True)
red.connect(ssid,password)

while red.isconnected() == False :
    print("Estableciendo conexión..")
    sleep(1)
    
print("Conexión Establecida")
print(red.ifconfig())