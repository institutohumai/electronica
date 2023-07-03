# Ejemplo N°19: Conectar la RPico W a una red WiFi y abrir un socket

import network
import socket 
from machine import Pin, ADC
from utime import sleep

ssid = 'CAMBIA POR TU SSID'
password = 'TU PASSWORD'

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

try:
    ip = connect()
    connection = open_socket(ip)
except KeyboardInterrupt :
    machine.reset()