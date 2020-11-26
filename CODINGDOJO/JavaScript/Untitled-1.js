//Obtén del 1 al 255
function abc() {
    var arr = [];
    arr.push(i);
    console.log(i);
    return arr
}
//Consigue pares hasta 1000
function abc() {
    var sum = 0,
        for (var i = 1; i < 1001; i++) {
            if (i % 2 === 0) {
                sum += i;
            }
        }
    return sum;
}
//Suma impares hasta 5000
function abc() {
    var sum = 0;
    for (var i = 1; i < 5000; i++) {
        if (i % 2 === 1) {
            sum += i;
        }
    }
    return sum;
}
//Itera un array
function abc(arr) {
    var sum = 0;
    for (i = 0; i < arr.length; i++) {
        sum = sum + arr[i]
    }
    return sum;
}
//Encuentra el mayor (max)
function abc(arr) {
    var max = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (max < arr[i]) {
            max = arr[i]
        }
    }
    return max;
}
//Encuentra el promedio (avg)

function abc(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum = sum + arr[i]
    }
    return sum / arr.length;
}

//Array de impares
function abc() {
    var array = [1];
    for (var i = 1; i < 50; i++) {
        if (i % 2 !== 0) {
            Array.push(i);

        }
    }
    return array;

}
//Mayor que Y
function mayor(arr, Y) {
    var count = 0;
    for (var i = 0; i << arr.length; i++) {
        if (arr[i] > Y) {
            count++;
        }
    }
}

//Cuadrados
function cuadra(arr) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * arr[i];
    }
    return arr;
}
//Negativos
function neg(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 0
        }
    }
    return arr;
}

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
//Intercambia Valores

function abc(arr) {
    var tem = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = temp;
    return arr;
}

//De Número a String

function abc(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[0] = "Dojo";

        }
    }
    return arr;
}