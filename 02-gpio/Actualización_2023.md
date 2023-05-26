Actualización Edición 2023: 

1. Respecto al LED onboard:

Si observamos el pinout de la **RPico** notaremos que está conectado a uno de los pines *GPIO* que posee el *RP2040*; el *GP25*. Recordemos que este es uno de los pines *GPIO* que no está disponible a los laterales de nuestra placa y solo puede utilizarse para comandar este *LED*. 

Pero, a diferencia de la **RPico**, el *LED* incorporado en la **RPico W** no está conectado a un pin del *RP2040*, sino a un pin *GPIO* del chip *CYW43439*. En términos de programación, solo cambiará la referencia al pin correspondiente como detallaremos se detalla a continuación:

```python
LED_onboard = Pin("LED", Pin.OUT)  # LED_onboard = Pin(25, Pin.OUT) si empleamos la RPico
```

2. Respecto a los esquemas de conexión:

Recordemos que la **RPico W** mantiene la compatibilidad de pines con la **RPico**, esto significa que la distribución de los 40 pines externos (que denominamos *pinout*) no cambia. Es por ello que, en los distintos esquemas de conexión que veamos a lo largo del curso, resulta indistinto si empleamos la **RPico** o la **RPico W**.

3. Respecto a los buzzer:

Se detalla la conexión para cuatro modelos distintos, incluido el *MH-FMD* que forma parte del kit. Si emplean otro modelo para llevar adelante los proyectos, y tienen dudas, por favor comuníquenla en Discord y los ayudamos.

4. Respecto al sensor PIR HC-SR501:

No se encuentra incluido dentro del kit, y no es necesario salir a comprarlo para aprobar el curso. El objetivo de esa sección es mostrar un ejemplo práctico de los temas desarrollados con un sensor que es fácil de adquirir si lo desean.