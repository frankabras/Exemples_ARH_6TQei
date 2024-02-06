#Importation des librairies utilisées
"""
Les différentes manières d'importer une librairie :
    import machine
    -> LED = machine.Pin(25,machine.Pin.OUT)
    from machine import Pin,PWM,ADC
    -> LED = Pin(25,Pin.OUT)
    from machine import *
    -> Idem que précédent mais importe tous les modules de la librairie
"""
import machine
"""
La librairie "machine" contient :
    -> Les fonctions d'entrées/sorties (Pin,PWM,ADC,...)
    -> Les fonctions de communications (UART, I3C,...)
    -> Les fonctions timers du microcontrôleur (Timer)
"""


#Définition des entrées/sorties
BUTTON = machine.Pin(16,machine.Pin.IN)	#On définit la pin 16 comme 
LED = machine.Pin(25,machine.Pin.OUT) 	#On définit la pin 25 comme sortie
#La pin 25 du Raspberry Pico est connectée à une led intégrée sur la carte

#Initialisation des variables 
bp_val = 0	#Variable utilisée pour stocker l'état de l'entrée
"""
Micro(Python) ne nécessite pas de spécifier le type de la variable (int,float,char,...) :
    -> maVariable = 12				=> Entier (int)
    -> maVariable = 1.2				=> Réel (float)
    -> maVariable = 'a'				=> Caractère (char)
    -> maVariable = "Hello World"	=> Chaine de caractères (char[n])
L'attribution du type se fait automatiquement par l'interpreteur
"""

print("Hello World")	#Permet d'afficher un message dans le terminal
"""
Autres possibilité avec la fonction print :

"""
while True:		#Comparable au while(1) {...} en langage C 
    bp_val = BUTTON.value()	#La fonction .value() pour récupérer l'état d'une entrée
    if bp_val == 1:		#Vérifie si l'entrée est active
        LED.on()		#La fonction .on() permet d'activer une sortie
        #LED.value(1)		#Autre méthode pour activer une sortie
        #LED.value(True)	#On peut également utiliser True
    else :			#Dans le cas ou l'entrée est incative
        LED.off()		#La fonction .off() permet de désactiver une sortie
        #LED.value(0)		#Autre méthode pour désactiver une sortie
        #LED.value(True)	#On peut également utiliser False