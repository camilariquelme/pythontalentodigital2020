#Básico : imprime todos los enteros del 0 al 150.

for x in range (0,151,1):
    print(x)

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000

for m in range (5,1000,5):
    print (m)

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. 
# Si es divisible por 10, imprima "Coding Dojo".


for x in range(1,101):
    print(x)
    if x % 10 == 0 :
        print("coding dojo")
        if x % 5 == 0:
            print("coding")
    x=x+1
    continue
print(x)
        

#hablar con el profe
#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.

suma=0
for i in range (1,500000):
    if i % 2 == 1:
        suma +=i
        
print(suma)

#Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.

for a in range (2018,0,-4):
    
    print (a)



#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3,
#  el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum=2
highNum=9
mult=2

for s in range(lowNum,highNum+1):
    if s % mult == 0:
        print(s)

