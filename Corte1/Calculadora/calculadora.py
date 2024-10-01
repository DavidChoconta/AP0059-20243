#David Ricardo Beltrán Chocontá - 20211005106
import clase


object1 = clase.Square(100)
print(f"From class Square: {object1.getVal()}")



object2 = clase.Add_Sub()

continuar = True

while continuar:
    
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    
    op = input("Ingrese qué operación quiere hacer (+, -, *, /): ")

    
    if op == '+': 
        print(f"La suma es: {object2.add(numero1, numero2)}")
    elif op == '-':
        print(f"La resta es: {object2.sub(numero1, numero2)}")
    elif op == '*':
        print(f"La multiplicación es: {object2.mul(numero1, numero2)}")
    elif op == '/':
        print(f"La división es: {object2.div(numero1, numero2)}")
    else: 
        print("Operador incorrecto")

    # Preguntar si el usuario desea realizar otra operación
    respuesta = input("¿Desea realizar otra operación? (si/no): ").lower()

    if respuesta != 'si':
        continuar = False
        print("Gracias por usar el programa.")
