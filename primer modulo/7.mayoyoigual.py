''' Un programa que pida dos números y que muestre cuál es mayor, cuál es menor o si son iguales (+3)'''
valor1= float(input("dije el valor 1: "))
valor2= float(input("dije el valor 2: "))

if(valor1 > valor2):
    print(" valor 1 es mayor", valor1 )
elif (valor2>valor1):
    print("valor 2 es mayor", valor2)
else:
    print("son iguales")
