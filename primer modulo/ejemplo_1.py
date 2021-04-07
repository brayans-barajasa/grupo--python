
ced=float(input("diguite la sedula "))
nhs=float(input("cuantoas horas trabajas a la semana"))
print("1 dedicacion por horas")
print("2 tiempo completo")
tipo=float(input(" tipo de empleado"))
if tipo ==1:
    sueldo=nhs*30000*4
if tipo==2:
    sueldo=nhs*20000*4

print("el sueldo del ciudadano con cedula a la semana es "+str(ced)+" es un total de :"+str(sueldo)+"pesos")   


