import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

points = 0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    #  Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        points += 6
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    #Paso la letra a lowercase para que usar en mayúscula no me coma intentos
    letter = letter.lower()

    # Verificar si el caracter ingresado es válido
    if (letter.isalpha() == False): # Método .isalpha(): chequea si está en el alfabeto
        print("Entrada no válida.")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        points -= 1
        print("Esa letra no está en la palabra.")

    print()
    
else:
    points = 0
    print(f"¡Perdiste! La palabra era: {word}")
print(f"Tenés un total de {points} puntos.")