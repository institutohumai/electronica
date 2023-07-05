# Ejemplo N°20: Primer proyecto IoT con la RPico W - Encendido del LED onboard y medición de la temperatura del RP2040

import network
import socket 
from machine import Pin, ADC
from utime import sleep

ssid = 'sala1eis'
password = 'sala1eis'

LED_onboard = Pin("LED", Pin.OUT)

sensor_temp = ADC(4)
factor_conversion = 3.3 / (65535)

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


def open_socket(ip):
    address = (ip,80)
    connection = socket.socket()   
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection
    
def webpage(temperature, state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <body>
        <form action="./lighton">
        <input type="submit" value="Encender LED" />
        </form>
        <form action="./lightoff">
        <input type="submit" value="Apagar LED" />
        </form>
        <p>El estado del LED es: {state}</p>
        <p>La temperatura del RP2040 es: {temperature}</p>
        </body>
        </html>
    """
    return str(html)

def serve(connection):
    state = 'APAGADO'
    LED_onboard.value(0)
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        #Comandar LED onboard
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            LED_onboard.value(1)
            state = 'ENCENDIDO'
        elif request =='/lightoff?':
            LED_onboard.value(0)
            state = 'APAGADO'
        #Monitorear temperatura del RP2040
        lectura = sensor_temp.read_u16() * factor_conversion
        temperature = 27 - (lectura - 0.706)/0.001721
        
        html = webpage(temperature, state)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt :
    machine.reset()