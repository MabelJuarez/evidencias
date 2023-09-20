while True:
    print("Menú:")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Hacer una suma")
    print("4. Hacer una resta")
    print("5. Hacer una multiplicación")
    print("6. Hacer una división")
    print("7. Salir")

    seleccion = input("Selecciona una opción: ")

    if seleccion == "1":
        binario = input("Coloque el numero binario: ")
        binario_rev = binario[::-1]
        longitud = len(binario)
        decimal = 0
        contador = 0
        while contador < longitud:
            if binario_rev[contador] == "1":
                decimal += 2**contador
            contador +=1

        print(decimal)

    elif seleccion == "2":
        
        decimal = input("Coloque el numero decimal: ")
        len(decimal)
        binario = ""
        cociente = int(decimal)
        while cociente != 1 :
            residuo =  cociente % 2
            cociente = cociente // 2
            binario = binario + str(residuo)

        binario = binario + str(residuo)
        res = binario [::-1]
        print(res)

    elif seleccion == "3":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resul = num1 + num2

        print(f"La suma de {num1} y {num2} es: {resul}")

    elif seleccion == "4":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resul = num1 - num2

        print(f"La resta de {num1} y {num2} es: {resul}")
        
    elif seleccion == "5":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resul = num1 * num2

        print(f"La multiplicación de {num1} y {num2} es: {resul}")    
        
    elif seleccion == "6":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resul = num1 / num2

        print(f"La división de {num1} y {num2} es: {resul}")

    elif seleccion == "7":
       exit()
        
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
        