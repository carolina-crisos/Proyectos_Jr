# Programa que identifica si un número dado es par o impar
print("Par o impar")
print("-" * 10)

while True:

    number = int(input("Ingresa un número entero: "))

    if number % 2 == 0:
        print(f'El número {number} es par.')
    else:
        print(f'El número {number} es impar.')

    ciclo = input("¿Deseas ingresar otro número? s/n: ")

    if ciclo.lower() == "s":
        continue
    else:
        print("Fin del programa.")
        break