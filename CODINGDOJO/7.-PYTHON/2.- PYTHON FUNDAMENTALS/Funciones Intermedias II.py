
#Actualiza los valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x[1])

students[0]['last_name']='Bryant'
print(students[0])

sports_directory['soccer'][0]="Andres"
print(sports_directory['soccer'])

#Itera a través de una lista de diccionarios

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


for i in range (0,len(students)):
    print('first_name -',students[i]['first_name'] , ',' 'last_name -',students[i]['last_name'])

#Obtén valores de una lista de diccionarios

for i in range(0,len(students)):
    print(students[i]['first_name'])

for i in range(0,len(students)):
    print(students[i]['last_name'])


#Itera a través de un diccionario con valores de listas

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print()
def list(dojo):
    
    for key in dojo:
        #print(key,dojo[key])
        print()
        print(key.upper(), len(dojo[key]))
        #print(dojo[key][0])
        for i in range (0,len(dojo[key])):
            print(dojo[key][i])

    

x=list(dojo)
