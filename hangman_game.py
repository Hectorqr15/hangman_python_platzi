import encodings
import os 

def run():
    print("funciona")

def menu():
    print(" 1.Iniciar Juego \n 2.Creador \n 3.Cerrar Juego")
    opcion = int(input("Por Favor Eliga una opción: "))
    try:
        if opcion == 1:
            os.system("clear")
            run()

        elif opcion ==2:
            os.system("clear")
            print("Hector Rafael")

        elif opcion ==3: 
            os.system("clear")
            print("Thanks ú! ")
            quit()

        else:
            raise ValueError("Inserte un valor válido")
    except ValueError as ve:
        os.system("clear")
        print(ve)
        menu()
        


if __name__ == "__main__":
    menu()
