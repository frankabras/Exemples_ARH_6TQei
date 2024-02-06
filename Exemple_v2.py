#Importation des librairies utilisées
import utime #Permet d'utiliser les foonctions tempo de MicroPython
from machine import Pin, PWM, ADC

#Déclaration de la fonction d'interruption du BP
"""
Une interruption est un mécanisme qui bloque le programme afin d'exectuer
un morceau de code lors d'un évènement particulier et qui reprend ensuite
le code à l'endroit où il s'était arreté

Dans ce cas-ci :
Le programme s'arrête lorsqu'on appuie sur un BP, pour executer la fonction
ci-dessous qui incrémente une variable et s'assure que sa valeur reste entre
0 et 4

Déclaration d'un fonction d'interruption :
    def nom_fonction(entrée1, entrée2,...,entréeN) :
        .
        .
        code de la fonction
        .
        .
        return sortie #permet de renvoyer une variable au programme principal

Utilisation de la fonction dans le code :
    sortie = nom_fonction(entrée1, entrée2,...,entréeN)
    
Dans le cas d'une inturreption, il n'est pas nécessaire d'utilisation la
fonction dans le code principale car elle est automatiquement appelée
lorsqu'on appuie sur le bouton poussoir

Par contre, il est ABSOLUMENT nécessaire d'indiquer le nom de l'entrée qui est
utilisée pour l'interruption, comme entrée de la fonction (*)
"""
def fonction_interruption(BUTTON): #*
    global state
    state = state + 1
    if state == 5:
        state = 0

#Définition des entrées/sorties
BUTTON = Pin(16,Pin.IN, pull=Pin.PULL_UP)	#On peut choisir une résistance de rappel
BUTTON.irq(trigger=Pin.IRQ_FALLING,handler=fonction_interruption)
"""
La ligne ci-dessus permet de lier l'interruption au BP et à la fonction à executer :
    trigger: Permet de choisir si l'interruption a lieue sur le front montant (passage 0->1)
             ou sur le front descendant (passage 1->0)
             - IRQ_RISING = front montant
             - IRQ_FALLING = front descendant
    handler: Permet de choisir la fonction à executer
"""

LED = Pin(25,Pin.OUT)

"""
Les sorties PWM (Pulses Width Modulation - Modulation de largeur d'impulsions) permettent
d'appliquer une tension variable à un éléments placer en sortie.
(Exemple d'utilisation : faire varier la luminosité d'une led)
"""
LED_PWM = PWM(Pin(17))
LED_PWM.freq(1_000) #Fréquence du signal PWM (plus spécifique)

"""
Les ADC (Analog to Digital Converter - Convertisseur Analogique-Digital) permmettent de
convertir une valeur analogique qu'on lui transmet en entrée et de la convertir en valeur
numérique utilisable par le microcontrôleur dans le programme
(Exemple d'utilisation : lire la valeur d'un potentiomètre)
"""
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
        #Permet de récupérer la valeur convertie par l'ADC 
        LED_PWM.duty_u16(pot_val)
        #Permet d'écrire la valeur PWM désirée (0 -> 65535 car 16bits)
        """
        Quelques valeurs d'exemple:
            -> PWM.duty_u16(0) 		= 0/65535 = 0 			=> 0 %
            -> PWM.duty_u16(16384) 	= 16384/65535 = 0,25	=> 25%
            -> PWM.duty_u16(32768) 	= 32768/65535 = 0,5 	=> 50%
            -> PWM.duty_u16(49152) 	= 49152/65535 = 0,75 	=> 75%
            -> PWM.duty_u16(65535) 	= 65535/65535 = 1 		=> 100 %
        """
    else :
        print("Etat inconnu")
        
