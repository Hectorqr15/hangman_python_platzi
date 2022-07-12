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
    
def normalize(s):
    s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def run():
    word = normalize(data())
    incognita = []
    print("Seleccione una letra: ")
    for i in range(len(word)):
        incognita.append(" - ")
    
    while list(word) != incognita: 
        print(word)
        print(incognita)
        #Que sola sea una letra con try
        try: 
            letra = input("Por favor digite una letra: ")
            if len(letra) > 1 or len(letra) == 0:
                raise ValueError("No mas de una letra")
            elif letra.isnumeric() == True:
                raise ValueError("Only String")
            else:
                for i in range(len(word)):
                    if letra == word[i]:
                        incognita[i] = letra
            os.system("clear")

        except ValueError as ve: 
            os.system("clear")
            print(ve)

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
