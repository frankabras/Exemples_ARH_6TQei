#Importation des librairies utilisées
import utime
from machine import Pin,PWM,ADC

#Déclaration de la fonction du BP
def fonction_interruption(BUTTON):
    global state
    state = state + 1
    if state > 4:
        state = 0

#Définition des entrées/sorties
BUTTON = Pin(16,Pin.IN, pull=Pin.PULL_UP)
BUTTON.irq(trigger=Pin.IRQ_FALLING,handler=fonction_interruption)

LED = Pin(25,Pin.OUT)

LED_PWM = PWM(Pin(15))
LED_PWM.freq(1_000)

POT = ADC(0)

#Initialisation des variables 
state = 0
pot_val = 0

while True:  
    #Gestion de la led
    if state == 0:
        LED.value(0)
    elif state == 1:
        LED.value(1)
        utime.sleep(0.5)
        LED.value(0)
        utime.sleep(0.5)
    elif state == 2:
        LED.value(1)
        utime.sleep(1)
        LED.value(0)
        utime.sleep(1)
    elif state == 3:
        LED.value(1)
    elif state == 4:
        LED.value(0)
        pot_val = POT.read_u16()
        LED_PWM.duty_u16(pot_val)
    else :
        print("Etat inconnu")
        

""" lecture du bouton
val = BUTTON.value()
if val == 1:
    state = state + 1
    if state > 4:
        state = 0
"""
