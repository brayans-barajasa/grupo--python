"""

crear un programa que le pida al usuario su edad, nombre, dos números y muestre por pantalla:


    - suma

    - resta

    - multiplicación

    - o división (dependiendo de la opcion)

    - de ambos números seguidos de su nombre y edad


    NOTA: si el usuario no es mayor de 5 años, no puede usar el programa

"""



'''


    ingrese su nombre

    ingrese su edad


    ingrese el primer numero 

    ingrese el segundo numero 



    1. suma

    2. resta

    3. multi

    4. division


    resultado de la operación : X 

    Nombre: 

    Edad: 

    

'''

nombre= str(input("ingrese su nombre: "))
edad= int(input("ingrese su edad: "))


if edad > 5:
    num1= float(input("ingrese su primer numero: "))
    num2= float(input("ingrese su segundo numero: "))
    ope=int(input("""
         1. suma

         2. resta

         3. multiplicacion

         4. division

         Escoja la operacion que deseas realizar:  """))
    print("")
    if ope== 1:
        print("la suma del primer con el segundo numero es igual a:", num1+num2)
    if ope== 2:
        print("la resta del primer con el segundo numero es igual a:", num1-num2)
    if ope== 3:
        print("la multiplicacion del  primer con el segundo numero es igual a:", num1*num2)
    if ope== 4:
        if num2 == 0:
            print("el segundo numero debe ser distinto a cero, para que la operacion sea correcta")
        print("la division del primer con el segundo numero es igual a:", num1/num2) 
        
    print("")
    print("nombre:", nombre)
    print("edad:", edad, "años")
else:
    print("debes ser mayor a 5 años, para poder utilizar el programa.")


