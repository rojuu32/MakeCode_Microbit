#Practica4
#Realizar un programa que muestre la suma de dos numeros al
#azar, uzando el punto A , en el lenguaje python para micro:bit.

#creamos dos variables
numero1=0
numero2=0
def on_button_pressed_a():
    global numero1, numero2
    numero1=randint(1,9)
    basic.show_number(numero1)
    basic.pause(500)
    basic.show_leds("""
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    """)
    basic.pause(500)
    numero2=randint(1,9)
    basic.show_number(numero2)
    basic.pause(500)
    basic.show_leds("""
    . . . . .
    # # # # #
    . . . . .
    # # # # #
    . . . . .
    """)
    basic.pause(500)
    basic.show_number(numero1-numero2)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
