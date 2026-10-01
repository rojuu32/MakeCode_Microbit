#practica 11
#Realiza un programa que simule un contador de numeros del 1 al 5
#usando FOR y el boton A, en el lengueje python
 
def on_button_pressend_a():

    for i in range(1,5+1):
      basic.show_number(i)
      basic.pause(300)

    #al terminar el bucle
    basic.show_icon(IconNames.YES)
    basic.show_string("FINAL")
    basic.pause(500)
    basic.clear_screen()
    
input.on_button_pressed(Button.A, on_button_pressend_a)
