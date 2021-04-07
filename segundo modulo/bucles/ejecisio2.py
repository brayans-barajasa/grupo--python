'''Escriba un programa que pida números decimales
mientras el usuario escriba número mayores que el primero. (+3)'''

n1=float(input("dijite su 1 numero"))
n2=float(input("dijite su  2 numero"))

while n2 > n1:
    n2=float(input("dijite su 2 numero"))
print(n2)