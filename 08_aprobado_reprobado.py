#practica 8
#Realiza un programa que muestre un sms, si el estudiante
#es aprobado o reprobado, usando numeros al azar y el 
#boton A, en el lenguaje python

numero=0
def on_button_pressed_b():
    global numero
    numero=randint(1, 100)
    basic.show_number(numero)
    basic.pause(1000)
    if numero >= 51:
        basic.show_string("APROBADO")
    else:
        basic.show_string("REPROBADO")
        basic.pause(500)
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
