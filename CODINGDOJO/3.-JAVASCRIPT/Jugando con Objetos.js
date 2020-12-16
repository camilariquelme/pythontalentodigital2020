var users = [{
    name: "Michael",
    age: 37
}, {
    name: "John",
    age: 14
}, {
    name: "David",
    age: 27
}];

//¿Cómo harías print/log de la edad de John?
console.log(users[1].age);

//¿Cómo harías print/log del nombre del primer objeto?
console.log(users[0].name);

//¿Cómo harías print/log del nombre y la edad de cada usuario utilizando un for loop?

for (let index = 0; index < users.length; index++) { //
    console.log(users[index].name, users[index].age);
}

//¿Cómo harías para imprimir el nombre de los mayores de edad?
for (let index = 0; index < users.length; index++) { //
    if (users[index].age > 18) {
        console.log(users[index].name);
    }
}

