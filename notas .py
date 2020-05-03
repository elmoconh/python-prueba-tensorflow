notas =0
contador =0
i=0


while i >=0:
    i = float(input('ingrese nota'))
    if (i >=0 and i < 8):
        notas = notas +i
        contador = contador+1
    else:
        print("ingrese un número correcto")

print (notas)
print(contador)
promedio= float(notas/contador)
print (promedio)