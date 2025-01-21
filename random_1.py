import random

print("Bienvenido al juego de Adivina el Número")
print("Adivina el número entre 1 y 100.")

numero_secreto = random.randint(1, 100)

intentos_restantes = 7

while intentos_restantes > 0:
    print(f"\nTe quedan {intentos_restantes} intentos.")
    try:
        adivina = int(input("Ingresa un número: "))
    except ValueError:
        print("Ingresa un número válido")
        continue

    if adivina < numero_secreto:
        print("El número es más alto")
    elif adivina > numero_secreto:
        print("El número es más bajo")
    else:
        print(f"Adivinaste el número {numero_secreto}.")
        break

    
    intentos_restantes -= 1

if intentos_restantes == 0:
    print(f"\n No te tienes más intentos. El número era {numero_secreto}. ¡Suerte la próxima!")
