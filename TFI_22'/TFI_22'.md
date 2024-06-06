# Clase N°5: Trabajo Final Integrador (TFI) - Monitoreo de Temperatura y Humedad relativa

![Figura 01 - Presentación TFI](./images/Figura01-PresentaciónTFI.jpg)  
*Figura 01 - Presentación TFI*

Concluida la etapa donde hemos incorporado los conceptos más importantes para trabajar con nuestra **Raspberry Pi Pico**, y con el objetivo de fortalecer los conocimientos adquiridos y promover que lleven a cabo sus propios proyectos, realizaremos un Trabajo Final Integrador (*TFI*) que combine las distintas herramientas que hemos aprendido durante el curso.

La propuesta del *TFI* implica resolver un problema real, que consiste en la medición de dos variables físicas (en este caso temperatura y humedad relativa), la visualización de los valores correspondientes en un display, y la emisión de una señal de alerta a un valor determinado. 

Para ello, desde el curso, se propone la utilización del *sensor de temperatura y humedad relativa DHT11*, o su variante más costosa *DHT22*, otorgando libertad de elección respecto a la estrategia a utilizar para concretar el *TFI*. 

Hablamos un poco acerca de estos sensores en la Clase N°1, pero profundizaremos la información de ellos, y veremos como se implementan y programan en nuestra *RPico* realizar nuestra *estación meteorológica*.

Empecemos!

![Figura 02 - Sensor DHT11 y DHT22](./images/Figura02-SensorDHT11yDHT22.jpg)  
*Figura 02 - Sensor DHT11 y DHT22*

## 5.1 Sensores DHT11 y DHT22: Características 

Por supuesto que si queremos realizar una estación meteorológica, debemos contar con sensores que nos proporcionen la información climática que precisamos. Existe una gran variedad de sensores en el mercado que permiten realizar esta tarea, pero nosotros nos detendremos en aquellos que sean compatibles con nuestra *RPico*. 

Cuando hablamos de compatibilidad, nos referimos puntualmente a aquellos sensores que nos proporcionan la información recolectada en un *tipo de dato* que pueda ser interpretado por nuestra *RPico*, y a la *alimentación* que requieren para su funcionamiento.

Recordemos que los sensores miden una magnitud física y responden a ella produciendo en su salida un *voltaje analógico* (Figura 03 de la Clase N°3) o un *voltaje digital* (Figura 02 de la Clase N°3). Los *sensores analógicos* son los que producen una *señal analógica* basada en lo que perciben, y de manera similar, los *sensores digitales* son los que producen una *señal digital* en respuesta a lo que miden en su entrada (Figura 03).

![Figura 03 - Señal de Salida de los Sensores](./images/Figura03-SeñaldeSalidadelosSensores.jpg)  
*Figura 03 - Señal de Salida de los Sensores*

En la Clase N°3, mencionamos un sensor analógico de temperatura muy conocido como es el [LM35](https://www.ti.com/lit/ds/symlink/lm35.pdf). Y también utilizabamos el sensor de temperatura interno del *RP2040*, otro ejemplo del tipo analógico, y vimos cómo se realizaba la lectura del valor sensado, llevando a cabo las conversiones correspondientes. Destacando que siempre utilizabamos las **entradas analógicas** de nuestra *RPico*, que se encuentran conectadas a los **ADCs** que posee nuestra placa. 

Sin embargo, para este *TFI*, utilizaremos un *sensor digital* como lo son el *DHT11*, o su variante más costosa, el *DHT22*. Estos sensores, además de medir la temperatura y la humedad relativa del ambiente, nos proporcionan una *salida digital*, volviéndolos más fáciles de implementar, ya que no necesitamos recurrir a las entradas analógicas de nuestro microcontrolador para realizar la lectura del valor medido. Además, son muy populares gracias a sus buenas prestaciones, bajo costo y fácil implementación.

Si bien ambos sensores lucen físicamente similares (varían en tamaño y color), y tienen la misma identificación de pines, poseen características diferentes que deben consultarse en las hojas de datos correspondientes [DHT11 Humidity & Temperature Sensor](https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf) y [DHT22 Humidity & Temperature Sensor](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf). De todas ellas, las diferencias más significativas se listan en la Figura 04.

![Figura 04 - Diferencias DHT11 y DHT22](./images/Figura04-DiferenciasDHT11yDHT22.jpg)  
*Figura 04 - Diferencias DHT11 y DHT22*

Como vemos, el tiempo de respuesta (es decir, el tiempo que tarda el sensor en ofrecer una lectura válida de la variable que esta midiendo), es menor en el *DHT11*. Sin embargo, el DHT22 tiene rangos de medida más amplios y mejor resolución, a cambio de resultar algo más caro. También observaremos, que ambos modelos pueden alimentarse con los pines que posee la *RPico*; *VBUS* si deseamos hacerlo con 5[Voltios] o *3V3(OUT)* si deseamos hacerlo con 3,3[Voltios]. 

La elección de un modelo u otro, dependerá del tipo de proyecto que queramos llevar a cabo. Para nuestro caso, la elección del *DHT11* es suficiente.

## 5.2 Sensores DHT11 y DHT22: Pinout y conexión 

En ambos sensores, los pines tienen el mismo orden y función (Figura 05). Si los miramos de frente y los enumeramos de izquierda a derecha, el primer pin es VCC, y lo conectaremos a los 5[Voltios] o 3,3[Voltios] de la *RPico*. En el otro extremo tenemos el pin 4 y es el GND, que irá conectado a un pin GND de la *RPico*. El pin 2 (DATA), es el que nos entregará la información de la temperatura y la humedad, y debe estar conectado a una **entrada digital** de la *RPico*. Y finalmente tenemos el pin 3 (NC), que no se utiliza debido a que no posee conexión eléctrica de ningún tipo. 

![Figura 05 - Pinout DHT11 y DHT22](./images/Figura05-PinoutDHT11yDHT22.jpg)  
*Figura 05 - Pinout DHT11 y DHT22*

Revisando las hojas de datos, veremos que en ambos modelos se debe colocar una resistencia entre el pin VCC y el pin DATA, cuyo valor debe estar entre 4700[Ohmios] y 10000[Ohmios], para que la lectura se realice sin problemas (el valor de la resistencia depende de la longitud del cable que conecta el sensor con la *RPico*). Esta configuración para una **entrada digital** ya la hemos visto en la Clase N°2: se trata de una *Resistencia Pull_Up* (Figura 06).

![Figura 06 - Esquema de Conexión DHT11 y DHT22](./images/Figura06-EsquemaDeConexiónDHT11yDHT22.jpg)  
*Figura 06 - Esquema de Conexión DHT11 y DHT22*

Debido a que el *DHT11* y *DHT22* poseen el mismo pinout, **las conexiones que realicemos para uno, son equivalentes para el otro**. Un ejemplo de conexión se muestra en la Figura 07. Como se puede ver, la alimentación del sensor está tomada del pin *3V3* (pin físico 36) y *GND* (pin físico 38), mientras que los datos se leen usando el pin *GP15* como entrada (pin físico 20).

Recordemos que la *RPico* incluye una resistencia programable integrada conectada a cada pin *GPIO*, que puede configurarse como resistencia *Pull_Down* o *Pull_Up* de acuerdo a nuestras necesidades, lo que nos ahorra la conexión de una resistencia física externa, reduciendo así la cantidad de elementos de nuestro circuito. Pero también recordemos, que por defecto, todos los pines están en *flotante*, por lo que debemos indicar *explícitamente* la configuración escogida en la función *Pin()*. Si no se indica al momento de la configuración del pin que utilicemos como entrada, debemos colocar la *Resistencia Pull_Up* externa como se indicó en la Figura 06. 

![Figura 07 - Conexión DHT22](./images/Figura07-ConexiónDHT22.jpg)  
*Figura 07 - Conexión DHT22*

Por otro lado, también es posible adquirir el *módulo sensor DHT11 (o DHT22)*. De forma similar a como ocurría con los zumbadores, este módulo incorpora el sensor correspondiente en una pequeña placa impresa. La diferencia entre ambos es que el módulo ya contiene una *Resistencia Pull_Up* incorporada. 

Algunos modelos también incluyen un pequeño capacitor en su parte posterior, que hace las veces de *filtro eléctrico* (es decir, para mitigar señales eléctricas externas no deseadas), y otros cuentan con un pequeño *LED* que nos avisa de su funcionamiento. (Figura 08)

![Figura 08 - Modelos del Módulo Sensor DHT11](./images/Figura08-ModelosDelMóduloSensorDHT11.jpg)  
*Figura 08 - Modelos Del Módulo Sensor DHT11*

En cualquiera de los modelos del *módulo sensor DHT11 (o DHT22)* que tengamos, veremos que el *Pin NC* de la Figura 05 ya no se encuentra, y que solamente expone los pines necesarios para su funcionamientos (Figura 09): *VCC* o *+*, *DATA* o *OUT*, y *GND* o *-*. De igual manera, siempre debemos prestar atención a la serigrafía impresa, para no confundirnos al momento de realizar las conexiones correspondientes.

![Figura 09 - Pinout Módulo Sensor DHT11](./images/Figura09-PinoutMóduloSensorDHT11.jpg)  
*Figura 09 - Pinout Módulo Sensor DHT11*

Un ejemplo de conexión del *módulo sensor DHT11 (o DHT22)* a nuestra *RPico* se muestra en la Figura 10. Como se puede observar, la alimentación del sensor está tomada del pin *3V3* (pin físico 36) y *GND* (pin físico 38), mientras que los datos se leen usando el pin *GP28* como entrada (pin físico 34).

![Figura 10 - Conexión Módulo Sensor DHT11](./images/Figura10-ConexiónMóduloSensorDHT11.jpg)  
*Figura 10 - Conexión Módulo Sensor DHT11*

## 5.3 Sensores DHT11 y DHT22: Transmisión de datos

Ambos sensores poseen en su estructura un conjunto de detectores de temperatura y humedad con una salida calibrada de señal en *formato digital*, gracias a que cuentan en un interior cuentan con un **Convertidor Analógico Digital (ADC)**, que se encarga de transformar las magnitudes analógicas en señales digitales. La entrega de la medición a otros circuitos (como nuestra *RPico*) se realiza mediante una *interfaz serie*. Recordemos, esto quiere decir que todos los datos van por una misma señal uno atrás del otro.

Sin embargo, ambos sensores no utilizan un protocolo de comunicación estándar como **I2C** o *SPI* para la transmisión de datos. En lugar de ello, implementan su propio protocolo para comunicarse a través de un solo hilo (DATA) con otros dispositivos, que es debidamente detallado en la hoja de datos. Afortunadamente, es un protocolo simple y puede implementarse sin problemas utilizando los pines digitales de nuestra *RPico*.

En resumen, podemos decir que, una vez realizado el proceso de conversión de analógico a digital, se establece un proceso de comunicación y sincronización entre la *RPico* y el sensor, en el cual este último envía una trama de datos de 40 bits (5 bytes) correspondientes a la información de humedad y temperatura como se muestra en la Figura 11.

![Figura 11 - Formato de datos DHT11](./images/Figura11-FormatoDeDatosDHT11.jpg)  
*Figura 11 - Formato de datos DHT11*

Como vemos, estos datos se interpretan de la siguiente manera:

1. El primer byte que recibimos es la *parte entera* de la *humedad relativa*.
2. El segundo byte es la *parte decimal* de la *humedad relativa*. En el caso que utilicemos el *DHT11*, este dato es siempre 0, ya que como describimos en la Figura 04, la resolución es del 1%. 
3. El tercer byte es la *parte entera* de la temperatura.
4. El cuarto byte es la *parte decimal* de la temperatura. En el caso que utilicemos el *DHT11*, este dato es siempre 0, ya que como describimos en la Figura 04, la resolución es de 1°C 
5. El quinto byte es la suma de verificación o *checksum*, resultante de sumar todos los bytes anteriores.

Este último byte se utiliza para corroborar que no existan datos corruptos en una transmisión de datos. Si la información recibida es correcta, al sumar los cuatro primeros grupos de bytes, el resultado debe ser igual al quinto byte. Tomemos como ejemplo la Figura 12, donde nuestra *RPico* ha recibido una trama como la ilustrada allí.

![Figura 12 - Ejemplo Trama de Datos DHT11](./images/Figura12-EjemploTramadeDatosDHT11.jpg)  
*Figura 12 - Ejemplo Trama de Datos DHT11*

Como dijimos, sumando los cuatro primeros grupos de bytes, debemos obtener el quinto. Si nos centramos en la trama de la Figura 12, comprobaremos que el dato recibido es correcto, ya que:

$\text{8 bits humedad + 8 bits humedad + 8 bits temperatura + 8 bits temperatura = 8 bits de checksum}$  
$0011 0101 + 0000 0000 + 0001 1000 + 0000 0000 = 0100 1101$

Al recibir la trama de datos, la *RPico* se encargará de sumar los cuatro primeros grupos de bytes. Si el resultado es igual al byte de *checksum* recibido, tomará los datos como válidos. Caso contrario, los descartará y esperará una nueva trama. 

Si volvemos a la hoja de datos, además de la trama, observaremos también, que todo el proceso de transmisión implica respetar unos tiempos determinados de inicio y finalización de comunicación entre el el microcontrolador y el sensor. Como estarán deduciendo, llevar a cabo la programación desde cero de todo el proceso implicaría mucho trabajo. 

Por suerte, la versión actual de **MicroPython** ya cuenta con librerías para este sensor, algo que nos permite ahorrar mucho tiempo de programación. Si queremos comprobar esto, nos situamos en la consola de Thonny con la *RPico* conectada y escribimos la instrucción *help("modules")* y veremos la librería *dht* correspondiente.

![Figura 13 - Librería dht en MicroPython](./images/Figura13-LibreríadhtenMicroPython.jpg)  
*Figura 13 - Librería dht en MicroPython*

## 5.4 TFI - Parte I: Puesta en marcha y lectura de valores

En esta primera parte del *TFI* veremos como se lleva a cabo la lectura de los valores arrojados por el *módulo sensor DHT11*, utilizando para ello, la librería *dht*. Utilizaremos en este caso, la conexión realizada en la Figura 10. Por supuesto, ustedes pueden emplear los pines correspondientes que deseen.

Y ahora a programar. Comencemos por conectar la *RPico* a nuestra computadora, ejecutar *Thonny* y hacer clic en el área de Script para cargar las librerías habituales, incorporando ahora la librería *dht*. Pero, como esta última está diseñada para los dos modelos del sensor DHT, importaremos únicamente la parte que posee todo lo necesario para manipular el *dht11*, quedando entonces:

```python
from machine import Pin
from utime import sleep
from dht import DHT11
```

Luego, debemos definir un objeto *dht* para poder leer los datos que provienen de nuestro sensor. En él, debemos indicar que pin utilizaremos como *entrada digital* (en nuestro caso, el *GP28*). Recordemos que no es necesario activar la *Resistencia Pull_Up* interna de nuestra *RPico*, ya que estamos utilizando el *módulo sensor DHT11*, y este ya cuenta con una *Resistencia Pull_Up* física incorporada:

```python
dht11_sensor = DHT11(Pin(28, Pin.IN))
```
Y ahora, para iniciar la transmisión de los valores que provienen del *DHT11*, debemos utilizar el método *measure()*. Luego, los métodos *temperature()* y *humidity()*, nos devolverán respectivamente la temperatura en grados Celsius y la humedad relativa en porcentaje. Almacenaremos estos valores en dos variables, quedando todo de la siguiente manera:

```python
dht11_sensor.measure()
temp = dht11_sensor.temperature()
hum = dht11_sensor.humidity()
```

Y ahora, debemos agregar un bucle que permita realizar esto de forma continua. Pero recordemos que el *DHT11* tiene un tiempo de respuesta de 1 segundo como se indicó en la Figura 04, entonces para respetar ese tiempo, agregaremos un delay levemente superior para garantizar la correcta lectura de los datos como se muestra a continuación: 

```python
while True:
    sleep(2)
    dht11_sensor.measure()
    temp = dht11_sensor.temperature()
    hum = dht11_sensor.humidity()
```

Para finalizar, se imprimen los valores obtenidos en la consola, utilizando la función *print()*. Dentro de ella, colocaremos entre comillas la cadena de caracteres que indique la magnitud que estamos midiendo, acompañada del valor correspondiente:

```python
    print('Temperatura: ',temp,'°C')
    print('Humedad Relativa: ',hum,'%')
    print() # Renglón en blanco 
```
Cuando ejecutes el código (ver *Ejemplo16_TFI_LecturaDHT11.py* en el repositorio), verás un mensaje como el de la Figura 14.

![Figura 14 - Lectura sensor DHT11](./images/Figura14-LecturaSensorDHT11.jpg)  
*Figura 14 - Lectura sensor DHT11*

Puedes comprobar el correcto funcionamiento cambiando las condiciones del espacio próximo al sensor, siempre con el debido cuidado de no dañar ningún componente. Por ejemplo, acerca la boca de un termo con agua caliente en su interior, y notarás que el vapor que sale modificará ambos valores.

## 5.5 TFI - Parte II: Visualizar datos medidos (Actividad N°1)

![Figura 15 - TFI - Parte II](./images/Figura15-TFIParteII.jpg)  
*Figura 15 - TFI - Parte II*

Ahora les toca a ustedes...

Como primera actividad, deben incorporar el *display LCD1602* al circuito que realizaron en la Parte I, y visualizar allí los datos de temperatura y humedad relativa. Recuerden que disponen de 16 caracteres por renglón. El resultado debe ser como el de la Figura 16.

![Figura 16 - TFI - Parte II - Ejemplo](./images/Figura16-TFIParteIIEjemplo.jpg)  
*Figura 16 - TFI - Parte II - Ejemplo*

Importante: El símbolo de grados "°" es un caracter especial y se escribe en el display mediante la instrucción *lcd.putstr(chr(223))*.

## 5.6 TFI - Parte III: Actuar (Actividad N°2)

Por último, a su pequeña *estación meteorológica* le incorporarán una señal de alarma, que se accione cuando ocurra una determinada condición. Para ello, al circuito de la Actividad N°1, deben sumarle una alarma lumínica (*LED*) o sonora (*Zumbador*), queda a elección de ustedes cual implementar. 

La condición a cumplir es que se accione cuando la humedad relativa sea superior al 70%.

¡Manos a la obra!

## 5.7 Condiciones de entrega del TFI

Para poder aprobar el *TFI*, la entrega debe contener todo lo realizado para resolver las actividades N°1 y N°2, esto incluye:

1. Foto del circuito implementado
2. Código completo realizado
3. Un video corto que demuestre el correcto funcionamiento de la *estación meteorológica*, donde se aprecie la visualización de los datos y el accionamiento de la alarma cuando se alcanza la condición fijada.

Fecha máxima de entrega: 23/12/22. Se atienden consultas de forma permanente por el canal de Discord. 