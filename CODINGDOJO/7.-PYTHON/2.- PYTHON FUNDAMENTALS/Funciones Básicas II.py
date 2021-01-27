#Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número 
# (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

num= int(input("Introduce un numero: "))
for i in range(1,num+1):
    print(int(num-i))

#Imprimir y volver : crea una función que recibirá una lista con dos números. 
# Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def f():
    num1= int(input("Introduce un numero: "))
    num2= int(input("Introduce un numero: "))
    print(num1)
    return(num2)
f()

#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de 
# la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

lista = [1,2,3,4,5]
num= 1

for x in lista:
    num = 1+ len(lista)

print(num)

#Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva 
# lista que contenga solo los valores de la lista original que sean mayores que su segundo valor.
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, 
# haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False


lista2 = []
def lista1 (x):
    for i in range(0, len(x)):
        if x[i] > x[1]:
            lista2.append(x[i])
    if len(lista2) > 2:
        print(len(lista2))
        return lista2
    else:
        return False
x = lista1([5,2,3,2,1,4])
print(x)

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def length_and_value (a,b):
    arreglo = []
    for p in range(0,a):
        arreglo.append(b)
    return arreglo
l = length_and_value(4, 7) 
print (l) 
