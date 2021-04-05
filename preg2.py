'''
Pregunta 2: Escriba un programa que elabore una lista de números pares e impares
dentro de un rango solicitado. Estos pueden ser ingresados en diferente orden
 y deberán ser almacenados en listas separadas, luego debe crear otra lista
  uniendo ambas listas, otra de suma y otra de multiplicar los elementos
   que luego deberá calcular el promedio. Debe imprimir ordenadamente lo solicitado.
'''

list_pares=[]
list_impares=[]

n = int(input("Digite la cantidad de numeros:   "))
for i in range(n):
    numero=int(input("ingrese el primer el numero: "))
    if numero%2==0:
        list_pares.append(numero)
    else:
        list_impares.append(numero)


list_union=list_pares+list_impares
lista_suma=[]

for i in range(len(list_pares)):
    lista_suma.append(list_pares[i] + list_impares[i])

lista_producto=[]

for i in range(len(list_pares)):
    lista_producto.append(list_pares[i] * list_impares[i])

# promedio de los numeros de la lista union
suma=0
for i in range(len(list_union)):
    suma=suma+list_union[i]

promedio=suma/len(list_union)


print(list_pares)
print(list_impares)
print(list_union)
print(lista_suma)
print(lista_producto)
print(promedio)






