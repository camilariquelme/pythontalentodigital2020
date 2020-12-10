//Dados un array y un valor Y, cuenta e imprime(print) el número de valores del array que sean mayores que Y.

//Mayor que Y
function mayor(arr, Y) {
    var count = 0;
    for (var i = 0; i << arr.length; i++) {
        if (arr[i] > Y) {
            count++;
        }
    }
}

//Dado un array, imprime los valores máximos (max), mínimos (min) y promedio (average) para el array.

//Max/Min/Avg:
function abc(arr) {
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];

        }
        if (arr[i] < min) {
            min = arr[i]
        }
        sum = sum + arr[i];
    }
    var fn = sum / arr.length;
    var arrnew = [max, min, fn];
    return arrnew;
}

//Dado un array de números, crea una función que dé como resultado un nuevo array donde los valores negativos 
//se reemplacen por el texto (string) ‘Dojo’. 
//Por ejemplo, reemplazarNegativos([1, 2, -3, -5, 5]) debiera devolver[1, 2, “Dojo”, “Dojo”, 5].

//Reemplazar Negativos

function abc(arr) {
    arrnew = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arrnew.push("dojo");
        } else {
            arrnew.push(arr[i]);
        }
    }
    return arrnew;
}
console.log(abc([1, 2, -3, -5, 6]));


//Dado un array y su respectivo índice, remueve los valores en el rango del índice dado( acortando el array). 
//Por ejemplo, removerRango([20, 30, 40, 50, 60, 70], 2, 4) debiera devolver[20, 30, 70].

function removerRango(arr, inicio, final) {
    intfallido = [];
    for (var i = 0; i < arr.length; i++) {
        if (i < inicio || i > final) {
            intfallido.push(arr[i]);


        }
    }
    return intfallido;
}
y = removerRango([20, 30, 40, 50, 60, 70], 2, 4);
console.log(y);