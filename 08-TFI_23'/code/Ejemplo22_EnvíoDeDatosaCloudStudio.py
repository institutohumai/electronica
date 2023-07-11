# Ejemplo N°22: Lectura del sensor de temperatura interno de nuestra Raspberry Pi Pico y envío de datos a CloudStudio

import network
import urequests as req	
from machine import Pin, ADC
from utime import sleep

ssid = 'CAMBIA POR TU SSID' # 'CAMBIA POR TU SSID'
password = 'TU PASSWORD' # 'TU PASSWORD'

sensor_temp = ADC(4)
factor_conversion = 3.3 / (65535)

# Esto se obtiene de la wiki de Cloud Studio
temperature_url = 'https://gear.cloud.studio/services/gear/DeviceIntegrationService.svc/UpdateTemperatureSensorStatus'

access_token = 'COLOCA TU ACCESS TOKEN' # 'COLOCA TU ACCESS TOKEN'

internal_temperature = 'COLOCA EL ENDPOINT ID CORRESPONDIENTE AL SENSOR INTERNO DE TEMPERATURA' # 'COLOCA EL ENDPOINT ID CORRESPONDIENTE AL SENSOR INTERNO DE TEMPERATURA'

payload_temperature = {
	'accessToken': access_token, # Se repite en todos los payloads que realicemos
	'endpointID': internal_temperature, # Es un numero entero y se modifica de acuerdo al sensor que utilicemos
	'temperatureCelsius': 30 # Valor inicial aleatorio
}

def connect():
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid,password)
    while red.isconnected() == False :
        print("Estableciendo conexión..")
        sleep(1)
    
    ip = red.ifconfig()[0]
    print("Conexión Establecida")
    print(red.ifconfig())
    return ip

def enviar_datos(ip):
    while True:
        # Realizo la lectura correspondiente
        lectura = sensor_temp.read_u16() * factor_conversion
        temperature = 27 - (lectura - 0.706) / 0.001721
        
        # La agrega el dato al payload
        payload_temperature['temperatureCelsius'] = temperature
        print('Tomando temperatura del sensor interno', payload_temperature['temperatureCelsius'])
        
        # Le envío al servidor y aguardo la respuesta del servidor (200)
        response = req.post(temperature_url, json = payload_temperature)
        print('Respuesta del servidor: ', response.status_code)
        response.close()
        sleep(1)
        
try:
    ip = connect()
    enviar_datos(ip)
except KeyboardInterrupt:
    machine.reset()