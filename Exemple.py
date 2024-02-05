#Importation des librairies utilisées
import utime
import machine
"""
import machine
    -> LED = machine.Pin(25,machine.Pin.OUT)
from machine import Pin,PWM,ADC
    -> LED = Pin(25,Pin.OUT)
from machine import *
    -> Idem que précédent mais importe tous
        les modules de la librairie
"""

#Définition des entrées/sorties
BUTTON = machine.Pin(16,machine.Pin.IN)
LED = machine.Pin(25,machine.Pin.OUT)

#Initialisation des variables 
bp_val = 0

print("Hello World")
while True:  
    bp_val = BUTTON.value()
    if bp_val == 1:
        LED.on()
        #LED.value(1)
    else :
        LED.off()
        #LED.value(0)