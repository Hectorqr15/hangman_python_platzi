import encodings
import os 
import random
import ast
from random import randint

def data():
    #data = []
    with open("./archivos/data.txt", 'r', encoding='utf-8') as f: 
        data = f.read().splitlines()
    return data[randint(0,len(data))]
    

def run():
    word = data()
    incognita = []
    print(word)
    print("Seleccione una letra: ")
    for i in range(len(word)):
        incognita.append(" - ")
    print(incognita)
    
    while list(word) != incognita: 
        #Que sola sea una letra con try
        letra= str(input("Por favor digite un numero: "))
        for i in range(len(word)):
            if letra == word[i]:
                incognita[i] = letra
                print(incognita)


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
