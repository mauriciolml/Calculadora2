def addmultiplenumbers(numbers):
    """Suma todos los números de la lista."""
    if not numbers:
        return 0  # Caso lista vacía
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """Multiplica todos los números de la lista en orden."""
    if not numbers:
        return 0  # Caso lista vacía
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    """Devuelve True si el número es entero y par, False si no."""
    if isitaninteger(num):
        return int(num) % 2 == 0
    return False

def isitaninteger(num):
    """Devuelve True si el número es entero (ej. 7 o 7.0), False si no."""
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

def main():
    print("¡Bienvenido a tu calculadora mejorada!\n")
    
    while True:
        print("Elige una opción:")
        print("1) Sumar varios números")
        print("2) Multiplicar varios números")
        print("3) Verificar si un número es par")
        print("4) Verificar si un número es entero")
        print("5) Salir")
        
        choice = input("Ingresa el número de la opción: ").strip()
        
        if choice == "1":
            nums = input("Ingresa los números separados por comas: ")
            try:
                numbers = [float(x) for x in nums.split(",") if x.strip() != ""]
                print("Resultado:", addmultiplenumbers(numbers))
            except ValueError:
                print("Error: Ingresa solo números válidos.")
        
        elif choice == "2":
            nums = input("Ingresa los números separados por comas: ")
            try:
                numbers = [float(x) for x in nums.split(",") if x.strip() != ""]
                print("Resultado:", multiplymultiplenumbers(numbers))
            except ValueError:
                print("Error: Ingresa solo números válidos.")
        
        elif choice == "3":
            num = input("Ingresa un número: ")
            try:
                number = float(num)
                print("Es par?", isiteven(number))
            except ValueError:
                print("Error: Ingresa un número válido.")
        
        elif choice == "4":
            num = input("Ingresa un número: ")
            try:
                number = float(num)
                print("Es un entero?", isitaninteger(number))
            except ValueError:
                print("Error: Ingresa un número válido.")
        
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        
        print("\n-----------------------------\n")

if __name__=="__main__":
    main()