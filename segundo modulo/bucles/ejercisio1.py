"""Escriba un programa que pida dos números enteros y escriba qué 
números impares desde el primero hasta el segundo. (+5)"""

b= int(input("primer numero: "))
s= int(input("segundo numero: "))

for  bi in range(b, s+ 2):
    if bi % 2 != 0:
        print(bi)
