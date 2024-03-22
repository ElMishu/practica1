import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
vocales= "a,e,i,o,u"
print("a" in vocales)

# Elegir una palabra al azar
secret_word = random.choice(words)

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
# Número máximo de intentos permitidos
print("Ingrese la cantidad de errores posibles: ")
max_fails = int(input())
print("Seleccione el nivel de dificultad:") 
print("(1) Fácil: En la palabra a adivinar se muestran todas las vocales por defecto.")
print("(2) Media: Se muestra la primer y la última letra de la palabra.")
print("(3) Difícil: No se muestra ninguna letra de la palabra")
dificulty= int(input())
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed=""
if dificulty == 1:
    letters = []
    for letter in secret_word:
         if letter in vocales:
             letters.append(letter)
         else:
             letters.append("_")
    word_displayed = "".join(letters)
  
if dificulty == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]


# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
fails=0
while fails < max_fails:
     # Pedir al jugador que ingrese una letra
     letter = input("Porfavor ingresa una letra valida: ").lower()
     while letter == '':             #chequea que no haya ingresado vacio
        letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         fails= fails+1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has llegado a los maximos fallos ({max_fails}).")
     print(f"La palabra secreta era: {secret_word}")