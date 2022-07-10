import encodings
import os 

def run():
    pass

def menu():
    print(" 1.Iniciar Juego \n 2.Creador \n 3.Cerrar Juego")
    opcion = input("Por Favor Eliga una opción: ")
    try:
        if opcion == '1':
            os.system("clear")
            run()

        elif opcion == '2':
            os.system("clear")
            print("hector rafael")

        elif opcion == '3': 
            os.system("clear")
            print("Thanks ú! ")
            quit()
        elif opcion.isnumeric() == False:
            raise ValueError("Only Numbers")

        else:
            raise ValueError("Inserte un valor válido")
    except ValueError as ve:
        os.system("clear")
        print(ve)
        menu()
        
def finish():
    print("Felicidades!")
    #perdiste o ganaste


if __name__ == "__main__":
    menu()
