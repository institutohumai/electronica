# Clase N°4: Protocolos de comunicación serie

![Figura 01 - Presentación Clase N°4](./images/Figura01-PresentaciónClaseN°4.jpg)  
*Figura 01 - Presentación Clase N°4*

Cuando conectamos periféricos a nuestra computadora, es fundamental contar con un **protocolo de comunicación** estandarizado que permita la interacción entre dichos periféricos y nuestro equipo. Dos de los protocolos más populares para este propósito son *USB* y *Ethernet*, aunque existen muchos otros en la actualidad. En el mundo de los **sistemas embebidos**, ocurre algo similar; a menudo, si deseamos conectar nuestro microcontrolador con otros dispositivos, también necesitamos hacer uso de un **protocolo de comunicación** estandarizado.

De todos los que existen, **UART (Universal Asynchronous Receiver-Transmitter)**, **SPI (Serial Peripheral Interface)** e **I2C (Inter-Integrated Circuit)** son los más conocidos, y todos ellos son implementables con nuestra **RPico W**. Aunque las características particulares de cada uno son sencillas, en el curso nos enfocaremos en **I2C** por una razón fundamental: es el más utilizado en el **Internet de las Cosas**.

Por ejemplo, en nuestros proyectos anteriores, dependíamos de la consola de **Thonny** para leer datos y utilizábamos nuestro monitor como medio de visualización. Sin embargo, en ciertos proyectos, es posible que no tengamos acceso a ambos recursos. En tales casos, necesitaremos otro hardware electrónico para realizar esta tarea. Una variedad de dispositivos de visualización resultan útiles en estas situaciones, como las pantallas *LCD*, *LED*, *OLED*, entre otros, que nos permiten transmitir información al usuario.

Cada una de estas pantallas tiene sus propias características como dispositivos de visualización y pueden utilizarse en diversos campos y aplicaciones según nuestros requisitos. Sin embargo, gran parte de ellas comparten una característica común: utilizan **I2C** como **protocolo de comunicación** para la transmisión de datos.

En la clase de hoy, nos enfocaremos en cómo usar un display *LCD* (del inglés, *Liquid-Crystal Display*) con módulo **I2C** integrado; exploraremos sus características, conexiones y las librerías necesarias para su funcionamiento. Esta dinámica de trabajo con un dispositivo en particular puede luego replicarse en otros dispositivos que implementen estos protocolos, lo que amplía el abanico de posibilidades para nuestros proyectos.

¡Empecemos!

## 4.1 Protocolo de comunicación I2C 

El protocolo **I2C** (también conocido como *Bus I2C* o *estándar I2C*) fue desarrollado por Philips Semiconductors (hoy NXP Semiconductors) en la década de los 80. Fue creado inicialmente para facilitar la comunicación entre varios chips dentro de los televisores fabricados por la compañía. Sin embargo, con el paso del tiempo, otros fabricantes comenzaron a adoptarlo hasta convertirse en el estándar que es hoy para conectar múltiples circuitos integrados digitales.

Además de los displays, existen una gran variedad de dispositivos que cuentan con conexión **I2C**, como el *módulo sensor de intensidad lumínica BH1750* y el *modulo sensor de distancia laser VL53L0x*, entre otros. Como mencionamos a lo largo del curso, es fundamental prestar atención a la hoja de datos del dispositivo que conectemos a nuestra **RPico W**.

![Figura 02 - BH1750 y VL53L0x](./images/Figura02-BH1750yVL53L0x.jpg)  
*Figura 02 - BH1750 y VL53L0x*

**I2C** funciona mediante una arquitectura *maestro-esclavo* (master-slave), donde se distinguen dos tipos de dispositivos:

1. *Maestro* (Master) o *Controlador* (Controller): son los que inician y coordinan la comunicación. En nuestro caso, emplearemos la **RPico W**.  
2. *Esclavos* (Slave) o *Periféricos* (Peripheral): son los dispositivos que están a la espera de que algún *maestro* se comunique con ellos. Esto puede incluir desde displays, sensores y actuadores, hasta memorias. Incluso es posible que un microcontrolador funcione como un esclavo en determinadas situaciones."

### 4.1.1 Descripción de las señales

El protocolo **I2C** requiere únicamente dos líneas de señal para su funcionamiento, como se muestra en la **Figura 03**: *SCL* y *SDA*. *SCL* (también denominada *SCK* o *SCLK*) es la señal de reloj y *SDA* es la señal de datos. 

![Figura 03 - Arquitectura I2C](./images/Figura03-ArquitecturaI2C.jpg)  
*Figura 03 - Arquitectura I2C*  

El **bus I2C** es *serie* (todos los datos van por una misma señal uno atrás del otro), *sincrónico* (una de las señales se usa para sincronizar y marcar el tiempo) y *half-duplex* (la comunicación *maestro-esclavo* es bidireccional, pero no de forma simultánea).

Es un protocolo bastante robusto y se puede usar con tramos cortos de cable de hasta 3 [metros]. Entre sus desventajas, podemos mencionar que su funcionamiento es un poco más complejo si lo comparamos con otros protocolos existentes, así como la necesidad de contar con una electrónica adicional para su implementación.

Para que la comunicación funcione de forma correcta se deben utilizar *resistencias PULL_UP* (resistencias conectadas a una tensión positiva), para asegurar un nivel alto cuando NO hay dispositivos conectados al **bus I2C**.

![Figura 04 - Esquema Eléctrico Bus I2C](./images/Figura04-EsquemaEléctricoBusI2C.jpg)  
*Figura 04 - Esquema Eléctrico Bus I2C*

En la **RPico W** no es necesario instalar estas resistencias cuando utilicemos este bus, ya que se activan de forma interna (de forma similar a lo que sucedía cuando implementábamos **entradas digitales** en la *Clase N°2*).

En el bus, cada dispositivo cuenta con una dirección, que se emplea para acceder a los dispositivos de forma individual. Esta dirección puede ser fijada por hardware (frecuentemente, mediante jumpers o pads) o totalmente por software.

En general, cada dispositivo conectado al bus debe tener una dirección única. Si tenemos varios dispositivos similares tendremos que cambiar la dirección o, en caso de no ser posible, implementar un bus secundario. El estándar actual de **I2C** permite acceder hasta un total de 112 dispositivos en un mismo bus, con una velocidad estándar de transmisión de 100[kHz],con un modo de alta velocidad de 400[kHz].

### 4.1.2 Implementación en nuestra RPico W

Para la implementación de este protocolo debemos utilizar los pines específicos que se muestran en la **Figura 05** marcados con color celeste. Como mencionamos, solo utilizaremos dos cables; uno para el canal de clock (*SCL*) y otro para el canal de datos (*SDA*). La **RPico W** posee dos buses **I2C** (I2C0 e I2C1), y pueden usarse uno o ambos, y son varios los pines físicos disponibles para ello.

![Figura 05 - Pines I2C de la RPico W](./images/Figura05-PinesI2CdelaRPicoW.jpg)  
*Figura 05 - Pines I2C de la RPico W*

## 4.2 Display LCD 1602 con módulo I2C: funcionamiento, características y conexión

Para demostrar el funcionamiento del **protocolo I2C**, utilizaremos un display LCD como el que se muestra **Figura 06**. Como mencionamos en la *Clase N°1*, este permite visualizar 16 caracteres alfanuméricos por renglón, en este caso, en los dos que dispone; de allí la denominación *display LCD1602*.

![Figura 06 - Display LCD 1602 Con Modulo I2C](./images/Figura06-DisplayLCD1602ConModuloI2C.jpg)  
*Figura 06 - Display LCD 1602 Con Modulo I2C*

Las pantallas LCD son unas de las formas más sencillas y económicas de dotar a nuestro proyecto de un medio de visualización de datos. El modelo que utilizaremos está basado en el controlador *Hitachi HD44780*, uno de los más utilizados debido a su sencillez y bajo precio. Si consultamos su hoja de datos [Hitachi HD44780 Datasheet](https://www.sparkfun.com/datasheets/LCD/HD44780.pdf), encontraremos que está diseñado para controlar *LCDs* monocromos de hasta 80 caracteres alfanuméricos y símbolos. También dispone de una pequeña memoria RAM para configurar nuestros propios caracteres o dibujos.

Realizar la conexión de este display de forma directa a un microcontrolador u otro dispositivo (**Figura 07**) requiere el empleo de una gran cantidad de cables, debido a que el envío de los distintos caracteres implica la utilización de al menos cuatro cables para el dato: *D4*, *D5*, *D6* y *D7*; más los cables necesarios para el control del display: alimentación (*GND* y *Vcc*), ajuste de contraste (*VO*), selección de registro (*RS*) , modo lectura/escritura(*R/W*) y habilitación (*E*).

![Figura 07 - Conexión directa Display 1602](./images/Figura07-ConexiónDirectaDisplay1602.jpg)  
*Figura 07 - Conexión directa Display 1602*

Como vemos, usar esta pantalla de forma directa requiere emplear una gran cantidad de pines de nuestra **RPico W** (además de una gran cantidad de código), lo que supone un enorme desperdicio de recursos. Una alternativa recomendable es usar un módulo que permita acceder al LCD a través del **bus I2C**. Si volteamos nuestro display, observaremos este módulo incorporado y soldado a nuestra placa. Puntualmente, el módulo que utiliza es el **PCF8574** que se muestra en la **Figura 08**.

![Figura 08 - Módulo PCF8574](./images/Figura08-MóduloPCF8574.jpg)  
*Figura 08 - Módulo PCF8574*

Este módulo **LCD-I2C** [PCF8574 Datasheet](https://www.ti.com/lit/ds/symlink/pcf8574.pdf) puede conectarse a cualquier LCD basado en el *Controlador Hitachi HD44780* y reduce la cantidad de cables necesarios a solo dos. Podemos adquirirlo de forma conjunta con el LCD, como así también de forma individual. 

La conexión es sencilla, simplemente alimentamos el módulo desde nuestra **RPico W** mediante *GND* y *VBUS*, y conectamos el pin *SDA* y *SCL* de la **RPico W** con los pines correspondientes del **PCF8574** como se ve en la **Figura 09**.

![Figura 09 - Esquema Conexión Módulo PCF8574](./images/Figura09-EsquemaConexiónMóduloPCF8574.jpg)  
*Figura 09 - Esquema Conexión Módulo PCF8574*

## 4.3 Descubriendo la dirección I2C de nuestro display LCD

Como mencionamos anteriormente, cada componente que conectamos al **bus I2C** tiene una dirección única, y cada mensaje y orden que transmitimos al bus, lleva anexa esta dirección, indicando cuál de los muchos posibles, es el receptor del mensaje.

Pero, claro, esto implica que sabemos de antemano la dirección del componente. El procedimiento normal es ir a la hoja de datos del dispositivo que deseamos conectar y allí encontrar la información que precisamos. Por ejemplo, el *módulo sensor de intensidad lumínica BH1750* que mencionamos anteriormente, en su hoja de datos [BH1750 Datasheet](https://datasheet.octopart.com/BH1750FVI-TR-Rohm-datasheet-25365051.pdf) nos indica que es posible configurarle dos direcciones para el bus **I2C**; *0x23* (0100011 en binario) o *0x5C* (1011100 en binario). Esta configuración se realiza en función de la tensión aplicada a un pin *ADDR* designado para este propósito.

Pero muy frecuentemente no disponemos de esta información, y debemos valernos de otro medio para obtenerla. Afortunadamente **MicroPython** tiene una solución para esto.

Tomemos nuestro *display LCD1602* como dispositivo del cual queremos conocer su dirección **I2C**, y lo conectamos como se muestra en la **Figura 10** con la ayuda de cables Dupont Macho-Hembra (M2F).

![Figura 10 - Conexión display LCD1602 a RPico](./images/Figura10-ConexiónDisplayLCD1602aRPico.jpg)  
*Figura 10 - Conexión display LCD1602 a RPico*

Como se observa, conectaremos el pin *VCC* del display al pin *VBUS* (cable color rojo), de forma que se alimente con 5[Voltios]. Además el pin *GND* debe conectarse a un pin homónimo de la **RPico W** (en la conexión de la **Figura 10**, se escogió el pin físico 38).

En este caso, y haciendo referencia a la **Figura 05**, escogimos los pines *I2C0 SDA* (pin físico 1) e *I2C0 SCL* (pin físico 2) de la **RPico W** para conectarlos a los correspondientes *SDA* y *SCL* del display.

Comencemos por conectar la **RPico W** a nuestra computadora. Y ya apreciarás que el display enciende su *backlight* (azul, verde o el color correspondiente al modelo).  

Luego ejecutemos **Thonny**, y en el área de Script carguemos las librerías habituales, incorporando ahora la función *I2C*:

```python
from machine import Pin, I2C
from utime import sleep
```

A continuación, haremos las siguientes definiciones:

```python
scl = Pin(1)
sda = Pin(0)
freq = 400000
```
Esto nos permite especificar los pines que utilizaremos para la comunicación, recordando que solo precisamos de dos señales en el **protocolo I2C**. Y por último establecemos velocidad de transmisión, en este caso, en su máximo valor posible de 400[kHz] (400000 [Hz]).

Y luego construimos el objeto *i2c* de la siguiente manera:

```python
i2c = I2C(0,sda=sda,scl=scl,freq=freq)
```

El primer argumento indica el bus **I2C** de la **RPico W** que utilizaremos, recordemos que cuenta con dos; *I2C0* e *I2C1*. El segundo y tercer argumento deben ser un objeto pin, que especifique cuál de ellos se utilizara para *SCL* (GP1) y *SDA* (GP0) respectivamente. Y el cuarto argumento, debe ser un número entero que establezca la velocidad máxima para SCL.

Por último, nos valdremos del método *scan()* que escanea todas las direcciones **I2C** en el bus especificado cuando creamos el objeto, entre las direcciones *0x00* y *0x77*, es decir un total de 120 direcciones. Recordemos que el estándar actual de **I2C** nos permite direccionar hasta un total de 112 dispositivos en un mismo bus.

Cada uno de los dispositivos que encuentre en el bus, los listará en un arreglo. Como solo hemos conectado un dispositivo **I2C**, vamos a obtener la dirección correspondiente en hexadecimal de la siguiente manera:

```python
direccion = hex(i2c.scan()[0])
```

Y finalmente imprimimos el valor obtenido:

```python
print('La dirección I2C es:', direccion)
```

Ejecutamos el código (ver *Ejemplo12_ObtenerDirecciónI2C.py* en el repositorio) y observaremos el valor **0x27** en nuestra consola, ¡es la dirección **I2C** de nuestro display!

Para comprobar esto, podemos dirigirnos a la hoja de datos del **PCF8574**. Allí veremos que el módulo dispone de 3 pads como se aprecia en la **Figura 11**; *A0*, *A1* y *A2*, con los cuales se selecciona la dirección **I2C**. Cuando ninguno está puenteado (como en nuestro caso), la dirección es **0x27** (en binario, 00100111). 

![Figura 11 - Pads del PCF8574](./images/Figura11-PadsDelPCF8574.jpg)  
*Figura 11 - Pads del PCF8574*

Estos pads seleccionan los 3 últimos dígitos binarios de la dirección. Al estar en circuito abierto, el dígito es '1'. Al estar puenteado, es '0'. Por ejemplo, si puenteamos A0 y A1, la dirección pasaría a ser '00100100' o **0x24**.

Con esto, comprobamos que el reconocimiento de la dirección **I2C** fue correcto. 

## 4.4 Instalación de librerías en Thonny

Hasta el momento hemos empleado librerías estándar de **MicroPython**, puntualmente *machine* y *utime*. Pero también existen aquellas librerías que han sido desarrolladas por los usuarios y la comunidad en general, que nos proporcionan funciones muy útiles para poder llevar a cabo nuestros proyectos. En la clase de hoy, utilizaremos una de ellas para controlar nuestro *display LCD 1602 con módulo I2C*. 

Primero debemos dirigirnos al siguiente repositorio [RPI-PICO-I2C-LCD](https://github.com/T-622/RPI-PICO-I2C-LCD), y luego descargarla como se muestra en la **Figura 12**, haciendo clic en *Code* y luego en *Download ZIP*.

![Figura 12 - Descarga librería RPI-PICO-I2C-LCD](./images/Figura12-DescargaLibreríaRPI-PICO-I2C-LCD.jpg)  
*Figura 12 - Descarga librería RPI-PICO-I2C-LCD*

Una vez descargada y descomprimida la librería, encontrarás seis archivos y tres de ellos con extensión *".py"*. Para que funcione la librería, debes pasar los archivos *lcd_api.py* y *pico_i2c_lcd.py* a la memoria de la **RPico W**. Esto lo podemos hacer desde **Thonny** con nuestra **RPico W** conectada.

Para ello, nos dirigimos a *Visualización* y luego a *Archivos*. En el panel que se abrirá a la izquierda de nuestra pantalla, buscamos la dirección donde están los archivos descargados.

Una vez allí, hacemos click derecho en *lcd_api.py* y seleccionamos *Subir a/*, de forma tal que este archivo pase a la memoria de nuestra **RPico W**. Luego repetimos lo mismo con el archivo *pico_i2c_lcd.py* (**Figura 13**).

![Figura 13 - Cargar archivos de librería en la RPico](./images/Figura13-CargarArchivosdeLibreriaEnLaRPico.jpg)  
*Figura 13 - Cargar archivos de librería en la RPico*

Si esto fue realizado de forma correcta, debemos encontrar estos dos archivos en la pestaña inferior *Raspberry Pi Pico* como se muestra en la **Figura 13**.

Esto indica que los archivos se encuentran dentro de la memoria flash de la **RPico W** y que ya podemos utilizarlos.

Para invocar cada una de estas librerías, debemos importarlas de la siguiente manera:

```python
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
```

## 4.5 Funciones de la librería RPI-PICO-I2C-LCD y ¡Hola Mundo! en el display LCD

Para comenzar a utilizar las funciones, primero debemos definir el **bus I2C** que utilizaremos de nuestra **RPico W**. Para ello, repetimos lo hecho anteriormente para el circuito de la **Figura 10**.

```python
scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)
```

Y luego debemos definir el objeto *lcd* para poder comandar nuestro display. Esto se realiza de la siguiente manera:

```python
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
```

Donde vemos que el primer argumento contiene todas las características del **bus I2C** implementado. El segundo argumento contiene la dirección del display a comandar, que ya la obtuvimos previamente y es *0x27*. Y por último, el tercer y cuarto argumento contiene el número de filas y columnas de nuestro display, en nuestro caso, 2 y 16 respectivamente. 

Con esta información, la definición correcta de nuestro display sería la siguiente:

```python
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
```
La documentación completa de todas las funciones que posee esta librería se encuentra en el archivo *README.md* que se aprecia en la **Figura 13**. De igual manera, un resumen de aquellas que utilizaremos se da a continuación. 

1. *lcd.putstr("Texto")*: Envía una cadena de caracteres al display. Para imprimir una variable debemos usar la instrucción *lcd.putstr(str (variable))*, que convierte la variable en una cadena.

2. *lcd.show_cursor()* / *lcd.hide_cursor()*: Mostrar / Ocultar el cursor del display.

3. *lcd.blink_cursor_on()* / *lcd.blink_cursor_off()*: Enciende / Apaga el cursor parpadeante al imprimir.

4. *lcd.backlight_on()* / *lcd.backlight_off()*: Enciende / Apaga la luz de fondo del display.

5. *lcd.display_on()* / *lcd.display_off()*: Enciende / Apaga el display (no el backlight, sino todo el chip).

6. *lcd.clear()*: Borra todos los caracteres o cualquier cosa escrita en el display.

7. *lcd.move_to(Col, Row)*: Mover a la posición indicada en *Col* y *Row*, respetando siempre los límites establecidos en *I2C_NUM_ROWS* e *I2C_NUM_COLS*. 

A esta altura ya debes estar ansioso por imprimir tu primer ¡Hola Mundo!, así que vayamos a ello. Continuaremos utilizando las conexiones del circuito de la **Figura 10**.

Como siempre, arrancamos por conectar la **RPico W**, ejecutar **Thonny** y hacer clic en el área de Script para cargar las librerías habituales, incorporando ahora todas las definiciones que hicimos hasta el momento que corresponden al **bus I2C** y al display LCD:

```python
from machine import Pin, I2C
from utime import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
```
Y ahora, debemos agregar un bucle que permita escribir de forma continua en nuestro display. Esto se logra de la siguiente manera:

```python
while True:
    lcd.clear() # Borra cualquier caracter previo que exista
    lcd.move_to(0,0) # Posiciona el cursor en el primer renglón y en la primera columna
    lcd.putstr("Hola Mundo!") # Escribir en la pantalla
    sleep(5)
```

Cuando ejecutes el código (ver *Ejemplo13_HolaMundoDisplayLCD* en el repositorio), verás un mensaje como el de la **Figura 14**.

![Figura 14 - Hola Mundo en el display LCD](./images/Figura14-HolaMundoEnElDisplayLCD.jpg)  
*Figura 14 - Hola Mundo en el display LCD*

## 4.6 Visualizar datos monitoreados
 
Por supuesto, no sirve de mucho una pantalla que solo dice *Hola Mundo!*. Para exponer el potencial de todo lo visto hasta el momento, recorramos algunos de los ejemplos realizados la clase anterior donde recogíamos datos provenientes del exterior.

Tomemos el *Ejemplo N°9* de la *Clase N°3*, donde realizamos la lectura del sensor de temperatura interno de nuestra **RPico W**, e incorporemos el display de la misma forma que en el circuito de la **Figura 10**. Al código debemos sumarle ahora, todo lo referido a **I2C** y al display, quedando de la siguiente manera (Ver *Ejemplo14_LecturayVisualizaciónTemperaturaRP2040* en el repositorio):

```python
from machine import Pin, ADC, I2C
from utime import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

sensor_temp = ADC(4)

factor_conversion = 3.3 / (65535)

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

while True:
    lectura = sensor_temp.read_u16() * factor_conversion
    temperatura = 27 - (lectura - 0.706)/0.001721
    
    lcd.clear() # Borra cualquier caracter previo que exista
    lcd.move_to(0,0) # Posiciona el cursor en el primer renglón y en la primera columna
    lcd.putstr("Temperatura: ") # Escribir en la pantalla
    lcd.move_to(0,1) # Posiciona el cursor en el segundo renglón y en la primera columna
    lcd.putstr(str (temperatura)) # Escribir en la pantalla
    sleep(5)
```

Ejecuta el código y visualizarás la temperatura de tu *RP2040* como se aprecia en la **Figura 15**.

![Figura 15 - Visualización Temperatura RP2040](./images/Figura15-VisualizaciónTemperaturaRP2040.jpg)  
*Figura 15 - Visualización Temperatura RP2040*

Tengamos en cuenta que en el ejemplo anterior estamos actualizando la lectura del sensor cada 5 segundos. Algunas aplicaciones requieren un tiempo menor, para que exista una correspondencia casi inmediata entre la variable que estamos monitoreando, y su visualización en el display. 

Un caso práctico de esto sería la lectura de un potenciómetro como el del *Ejemplo N°8* de la *Clase N°3*. Repite la conexión realizada en la clase pasada e incorpora ahora el display de la misma forma que en el circuito de la **Figura 10**.

En cuanto al código, nuevamente debemos sumarle todo lo referido a **I2C** y al display, quedando de la siguiente manera (Ver *Ejemplo15_LecturayVisualizaciónPotenciómetro* en el repositorio):

```python
from machine import Pin, ADC, I2C
from utime import sleep
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

potenciometro = ADC(26)

factor_conversion = 3.3 / (65535)

scl = Pin(1)
sda = Pin(0)
freq = 400000

i2c = I2C(0,sda=sda,scl=scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

while True:
    voltaje = potenciometro.read_u16() * factor_conversion

    lcd.clear() # Borra cualquier caracter previo que exista
    lcd.move_to(0,0) # Posiciona el cursor en el primer renglón y en la primera columna
    lcd.putstr("Voltaje: ") # Escribir en la pantalla
    lcd.move_to(0,1) # Posiciona el cursor en el segundo renglón y en la primera columna
    lcd.putstr(str (voltaje)) # Escribir en la pantalla
    sleep(1)
```

Ejecuta el código y gira la perrilla del potenciómetro completamente en una dirección y luego completamente en la otra. Observarás los valores que antes imprimías en consola, pero ahora en tu display LCD como se aprecia en la **Figura 16**.

![Figura 16 - Visualización de los valores de un potenciómetro](./images/Figura16-VisualizaciónDeLosValoresDeUnPotenciómetro.jpg)  
*Figura 16 - Visualización de los valores de un potenciómetro*

¡Felicitaciones! Has aprendido los principales conceptos acerca de **I2C** y su aplicación para visualizar datos en un display LCD.

## 4.7 Protocolo de comunicación SPI

**SPI** es un protocolo alternativo y similar a **I2C** que se utiliza en numerosos dispositivos. A diferencia de este último, permite una velocidad de transmisión superior, pero requiere un mayor número de pines para su implementación.

El protocolo **SPI** (a veces también denominado **"Bus SPI"** o **"estándar SPI"**), nace a principios de los 80s cuando Motorola lo empieza a introducir y desarrollar para sus microcontroladores. Posteriormente fue adoptado por otros fabricantes como Microchip y Atmel, hasta convertirse en un estándar de comunicación con bastante aceptación en la industria. 

Numerosos dispositivos cuentan con **SPI** para su funcionamiento, entre ellos el *Módulo Lector RFID RC522*, ampliamente utilizado en sistemas de identificación y control de acceso con tarjetas y llaveros RFID.

![Figura 17 - Módulo Lector RFID RC522 con tarjetas y llaveros RFID](./images/Figura17-MóduloLectorRFIDRC522conTarjetasyLlaverosRFID.jpg)  
*Figura 17 - Módulo Lector RFID RC522 con tarjetas y llaveros RFID*

En la actualidad, es cada vez más frecuente encontrar dispositivos que incorporan tanto la conexión **SPI** como **I2C** para facilitar la integración de proyectos, ya que ofrecen una mayor flexibilidad al momento de elegir el **protocolo de comunicación**. Un ejemplo destacado de esto es el *módulo sensor de presión y temperatura BMP280*.

![Figura 18 - Modulo Sensor de Presión y Temperatura BMP280](./images/Figura18-ModuloSensorDePresiónyTemperaturaBMP280.jpg)  
*Figura 18 - Modulo Sensor de Presión y Temperatura BMP280*

Al igual que **I2C**, **SPI** funciona con una arquitectura *maestro-esclavo*, pero la dirección de los dispositivos no se transmite por el canal de datos, sino que se utilizan pines específicos para seleccionarlos como veremos a continuación.

### 4.7.1 Descripción de las señales

Requiere de cuatro líneas de señal para su funcionamiento como se aprecia en la **Figura 19**; *MOSI*, *MISO*, *SCLK* (a veces también denominada *SCK* o *SCL*) y *SS* (a veces también denominada *CE* o *CS*):

1. MOSI (*Master Out, Slave In*): Salida de datos para el maestro, entrada de datos para el esclavo.
2. MISO (*Master In, Slave Out*): Entrada de datos para el maestro, salida de datos para el esclavo.
3. SCLK (*Serial CLocK*): Señal de reloj respecto a la que se sincronizan el resto de las señales.
4. SS (*Slave Select*): Señal utilizada para seleccionar el esclavo con el que el maestro desea comunicarse.

![Figura 19 - Bus SPI: un maestro y un esclavo](./images/Figura19-BusSPIUnMaestroYUnEsclavo.jpg)  
*Figura 19 - Bus SPI: un maestro y un esclavo*  

En **Electrónica Digital**, una barra horizontal sobre un pin como en el caso de *SS*, se utiliza para indicar que la activación del mismo se realiza enviando una señal binaria de *valor lógico 0* o *LOW*.

En la **Figura 19** se muestra un **Bus SPI** que consta solamente de un *maestro* y un *esclavo*. Sin embargo, añadiendo varias líneas *SS* (por ejemplo *SS1*, *SS2* y *SS3*) se puede implementar un **Bus SPI** con muchos *esclavos*, todos controlados por el mismo *maestro*, como se muestra en la **Figura 20**.

![Figura 20 - Bus SPI: un maestro y tres esclavos independientes](./images/Figura20-BusSPIUnMaestroYTresEsclavosIndependientes.jpg)  
*Figura 20 - Bus SPI: un maestro y tres esclavos independientes* 

La conexión de la **Figura 20** se denomina *configuración de esclavos independientes*, y como se aprecia, es necesario contar con hardware adicional o **salidas digitales** dedicadas (pines *SS*), controladas por el maestro, para seleccionar el *esclavo* conectado al bus con el que deseamos comunicarnos. 

Como vemos, no hay límite para la cantidad de dispositivos **SPI** que se pueden conectar. Sin embargo, existen límites prácticos debido al número de líneas de selección de hardware disponibles en el maestro (pines *SS*) en la *configuración de esclavos independientes*. 

El **bus SPI** es *serie* y *sincrónico* al igual que el **bus I2C**, pero a diferencia de este último, es un protocolo *full-duplex*, ya que permite la comunicación *maestro-esclavo* de forma bidireccional y simultánea. Y como vimos, cada *esclavo* requiere una señal de habilitación separada, incrementando la complejidad en el conexionado si lo comparamos con **I2C**.

Es un protocolo diseñado para aplicaciones de trasmisión de datos a velocidades altas (superiores a las de **I2C**) y distancias cortas (del orden de 10 a 20[cm]), o para ser implementado dentro de una *placa de circuito impreso* (PCB).

Además, no requiere *resistencias pull-up* o *resistencias pull-down* para su funcionamiento básico. Sin embargo, en casos particulares, podría ser necesario utilizarlas en las líneas de datos (*MOSI* y *MISO*) para garantizar niveles de voltaje adecuados en el **bus SPI**. Por ejemplo, si se están utilizando pines de propósito general (*GPIO*) de un microcontrolador, es posible que se las necesite para garantizar niveles de señal estables cuando los *esclavos* no estén activamente conduciendo en el bus. En resumen, la necesidad de estas resistencias dependerá de la implementación específica del sistema y de los dispositivos utilizados.

### 4.7.2 Implementación en nuestra RPico W

Para la implementación de este protocolo debemos utilizar los pines específicos que se muestran en la **Figura 21** marcados con color fucsia. Y como mencionamos, necesitaremos cuatro cables; *MOSI*, *MISO*, *SCLK* y *SS*. La **RPico W** posee dos buses **SPI** (SPI0 y SPI1), y pueden usarse uno o ambos, y son varios los pines físicos disponibles para ello.

![Figura 21 - Pines SPI de la RPico W](./images/Figura21-PinesSPIdelaRPicoW.jpg)  
*Figura 21 - Pines SPI de la RPico W*

Sin embargo, encontrarás una leve modificación en los nombres de los pines. En el pinout, se denominan *SPI TX* (transmisión) y *SPI RX* (recepción) a los pines de comunicación de datos. Esto se debe a que la **RPico W** puede ser un dispositivo *maestro* o *esclavo*, por lo que estos pines serán *MOSI* o *MISO* dependiendo de la función que cumpla la **RPico W**.

## 4.8 Protocolo de comunicación UART

**UART** es uno de los primeros y más simples **protocolos de comunicación** *serie* para el intercambio de datos entre dos dispositivos. A diferencia de **I2C** y **SPI**, la comunicación **UART** se realiza de forma *asíncrona*, es decir, no requiere una señal de reloj para sincronizar la comunicación entre los dispositivos.

Al no necesitar una fuente de reloj común entre el transmisor y el receptor, ambos lados operan según sus relojes independientes. Sin embargo, existe un concepto clave llamado *tasa de baudios*, que ayuda a mantener sincronizados estos dispositivos al definir la velocidad de intercambio de datos.

La *tasa de baudios* se refiere a la cantidad de bits de datos transmitidos por segundo. Por lo tanto, los dispositivos que se comuniquen empleando **UART** deben funcionar a la misma *tasa de baudios* para asegurar un funcionamiento correcto. El valor de *9600 baudios* es el más ampliamente aceptado en la industria de la electrónica y es soportado por casi todos los dispositivos que utilizan **UART** para comunicarse.

Algunos dispositivos que utilizan **UART** para su funcionamiento son el *Módulo Bluetooth HC-05* y el *Módulo GPS NEO-6M*. 

![Figura 22 - Módulo Bluetooth HC-05 y Módulo GPS NEO-6M](./images/Figura22-MóduloBluetoothHC-05yMóduloGPSNEO-6M.jpg)  
*Figura 22 - Módulo Bluetooth HC-05 y Módulo GPS NEO-6M*

### 4.8.1 Descripción de las señales

**UART** utiliza únicamente dos señales, conocidas como *Rx* y *Tx*. El pin *Tx* de un dispositivo transmite datos al pin *Rx* de otro dispositivo, y viceversa: el pin *Tx* de este último transmite datos al pin *Rx* del dispositivo anterior. Este intercambio de datos se aprecia en la **Figura 23**. Como podrás observar, solo dos dispositivos pueden comunicarse de forma simultánea, lo que representa la principal limitación de **UART**.

![Figura 23 - Arquitectura UART](./images/Figura23-ArquitecturaUART.jpg)  
*Figura 23 - Arquitectura UART*

### 4.8.2 Implementación en nuestra RPico W

Para la implementación de este protocolo debemos utilizar los pines específicos que se muestran en la **Figura 24** marcados con color lila. Y como mencionamos, necesitaremos dos líneas de comunicación; *TX* y *RX*. La **RPico W** posee dos buses **UART** (*UART0* y *UART1*), y pueden usarse uno o ambos, siendo varios los pines físicos disponibles para ello.

![Figura 24 - Pines UART de la RPico W](./images/Figura24-PinesUARTdelaRPicoW.jpg)  
*Figura 24 - Pines UART de la RPico W*

## 4.9 Conclusión y resumen

Entonces, ¿cuál es el mejor **protocolo de comunicación serie**? Lamentablemente, no existe uno que podamos llamar "el mejor". Como hemos visto, cada uno tiene sus propias ventajas y desventajas, por lo que cada usuario deberá elegir según sus necesidades. Puede que uno se adapte mejor a tu proyecto, o quizás ya tengas a disposición un componente con **I2C**, **SPI** o **UART**.

Si te encuentras indeciso sobre cuál protocolo es el adecuado para tu proyecto, se recomiendan estos breves consejos:

1. Cuando priorices la velocidad de transferencia de datos, el protocolo **SPI** será tu mejor opción de comunicación.

2. Si tu proyecto implica la comunicación con varios dispositivos y deseas mantener una conexión cableada relativamente simple, la elección preferida sería el protocolo **I2C**.

3. Si tu proyecto se centra únicamente en la transferencia de datos entre dos dispositivos de forma transparente, **UART** es la solución más simple y rentable, especialmente para aplicaciones con recursos de hardware limitados.