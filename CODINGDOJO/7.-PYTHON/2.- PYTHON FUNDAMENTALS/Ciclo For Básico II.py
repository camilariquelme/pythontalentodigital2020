# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def biggie_size(arr):
    for i in range (0,len(arr)):
        if (arr[i] > 0):
            arr[i] = "Big"
        else:
            arr[i]=arr[i]
    return arr

arr=biggie_size([-1, 3, 5, -5])
print(arr)

# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el 
# número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def count_positives(d):
    sum=0
    for i in range(0,len(d)):
        if d[i]>0:
            sum=sum+1
    else:
        d[len(d)-1]=sum 
    return d
    
d = count_positives ([1,6, -4, -2, -7, -2])
print(d)

# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(r):
    total = 0
    for o in range(0,len(r)):
        total=r[o]+total
            
    return(total)
r =sum_total ([1,2,3,4])
print (r)

# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(prom):
    sume=0
    tot=0
    for q in range(0,len(prom)):
        sume=prom[q]+sume
        tot=sume/len(prom)
    return tot
prom=promedio([1,2,3,4]) 
print (prom)



# Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud(k):
    sumi=0
    for i in range(0,len(k)):
        sumi= 0+ len(k)
    return sumi
k=longitud ([37,2,1, -9]) 
print (k)

# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def minimo (u):
    if len(u)==0:
        return False
    else:
        minimot = u[0]
        for t in range (0, len(u)):
            if u[t]<minimot:
                minimot = u[t]
        return minimot
u = minimo ([37,2,1, -9])
print(u)#output: -9


# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def maximo(x):
    if len(x)==0:
        return False
    else:
        maxim = x[0]
        for i in range (0, len(x)):
            if x[i]>maxim:
                maxim = x[i]
        return maxim
x = maximo([37,2,1, -9])
print(x)

# Análisis final : crea una función que tome una lista y devuelva un diccionario 
# que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 
# 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

def ultimate_analysis(x):
    minimo1=0
    maximo1=0
    promedio=0
    long=0
    suma=0
    for i in range(0,len(x)):
        if x[i]>maximo1:
                maximo1 = x[i]
        if x[i]<minimo1:
                minimo1 = x[i]
        long= 0+ len(x)
        suma= suma + x[i]
        promedio= suma /len(x)
    ultimate_analysis= {"total":suma, "maximo": maximo1, "minimo":minimo1,"promedio":promedio,"longitud":long}
    return ultimate_analysis
x= ultimate_analysis([37,2,1, -9])
print(x)

# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

reverse_list = [37,2,1, -9]
print("La lista es: ", reverse_list)
reverse_list1 = reverse_list[::-1]
print("Lenguajes invertidos son:", reverse_list1)