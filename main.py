print("Hola Jeanca")
print("1.sumar")
print("2.restar")
print("3.salir")
print("\n")

op = 0

while op != 5:
    op = int(input("Ingresa una opcion: "))

    match op:

        case 1:
            print("--SUMA--")
            num1=int(input("Ingresa el primer numero: "))
            num2=int(input("Ingresa el segundo numero: "))

            result = num1 + num2

            print(f"El resultado es: {result}")

        case 2:
            print("--RESTAR--")
            num1=int(input("Ingresa el primer numero: "))
            num2=int(input("Ingresa el segundo numero: "))

            result = num1 - num2
            print(f"El resultado es: {result}")



