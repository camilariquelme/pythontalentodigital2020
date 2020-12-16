//Tamaño Grande

function abc(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            arr[i] = "Big";
        }
    }
    return arr;


}
console.log(abc([-1, 3, 5, -5]));

//Imprime (print) el menor, devuelve (return) el mayor

function abc2(arr) {
    var max = arr[0];
    var min = arr[0];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];

        }

    }
    console.log(min);
    return max;

}

arr = abc([-1, 3, 5, -5]);

//Imprime (print) uno, devuelve (return) otro

function abc2(arr) {
    console.log(arr[arr.length - 2]);
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 != 0) {
            return arr[i];

        }

    }

}

arr = abc2([4, 3, 5, -5]);

//Doble Visión

function vision(arr) {

    var vision2 = [];
    for (var i = 0; i < arr.length; i++) {
        vision2.push(2 * arr[i]);

    }
    return vision2;
}
arr = vision([1, 2, 3]);


//contar positivos

function pos(arr) {
    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            count = count + 1;
        }
    }
    arr[arr.length - 1] = count;
    return arr;

}

console.log(pos([-1, 1, 1, 1]));

//Pares e Impares
function par(arr) {
    var sum = 0;
    var sum2 = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            sum = sum + 1;
            sum2 = 0;
            if (sum == 3) { console.log("que bien"); }

        } else {
            sum2 = sum2 + 1;
            sum = 0;
            if (sum2 == 3) { console.log("que imparcial"); }

        }
    }
}
console.log(par([8, 2, 6, 1, -5, 3]));

//incrementa los segundos

function segund(array) {
    for (let i = 0; i < array.length; i++) {
        if (i % 2 != 0) {
            array[i] = array[i] + 1;
            console.log(array[i]);
        }
    }
    return array;
}
console.log(segund([1, 2, 3, 4, 5, 6, 7, 8]));

//longitudes previas
//Pasado un array (similar a decir ‘tomado un array’ o ‘dado un array’) que contiene strings, 
//reemplaza cada string con un número de acuerdo cantidad de letras (longitud) del string anterior. 
//Por ejemplo, longitudesPrevias([“programar”,“dojo”, “genial”]) debería devolver [“programar”,9, 4]. 
//Pista: ¿For loops solo puede ir hacia adelante ?

function long(arr) {

    for (var i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i - 1].length;
    }
    return arr;
}
console.log(long(['logo', 'programar', 'dojo', 'genial']));

//Agrega Siete

//Construye una función que acepte un array. Devuelve un nuevo array con todos los valores del original, 
//pero sumando 7 a cada uno. 
//No alteres el array original.Por ejemplo, agregaSiete([1, 2, 3) debería devolver[8, 9, 10] en un nuevo array.


function agrega(arr) {
    var sum = 7;
    for (var i = 0; i < arr.length; i++) {
        arr[i] = sum + arr[i];


    }
    return arr;
}
console.log(agrega([1, 2, 3]));

//Array Inverso

//Dado un array, escribe una función que invierte sus valores en el lugar.
//Ejemplo: invertir([3,1,6,4,2)) devuelve el mismo array pero con sus valores al revés,
// es decir [2,4,6,1,3]. Haz esto sin crear un array temporal vacío. (Pista: necesitarás intercambiar (swap) valores).

function inv(arr) {
    var temp = arr[0];
    arr[0] = arr[arr.length - 1]; {
        arr[arr.length - 1] = temp;
    }
    arr[1] = arr[arr.length - 2]; {
        arr[arr.length - 2] = temp;
    }
    return arr;
}
console.log(inv([3, 1, 6, 4, 2]));

//Perspectiva: Negativa
//Dado un array crear y devuelve uno nuevo que contenga todos los valores del array original, 
//pero negativos (no simplemente multiplicando por -1). Dado [1,-3,5], devuelve [-1,-3,-5].

function neg(arr) {
    arrnew = [];
    for (var i = 0; i < 0; i++) {
        if (arr.length < 0) {
            arrnew.push(i);
        }
    }
    return arrnew;
}
console.log(neg([1, -3, 5]));
console.log(arrnew);

//Siempre hambriento
//Crea una función que acepte un array e imprima (print) “yummy” 
// cada vez que alguno de los valores sea “comida”. Si ningún valor es “comida”,
//entonces imprime “tengo hambre” una vez.

function hambriento(array) {
    var num = 0; 
    for (let i = 0; i < array.length; i++) {
        if (array[i] == 'comida') {
            num = num + 1;
            console.log('yummy');
        }
    }
    if (num == 0) {
        console.log('tengo hambre');
    }
}
console.log(hambriento([1, 2, 3, 'comida', 5]));


//Cambiar hacia el centro -  Dado un array, cambia el primer y último valor, el tercero con el ante penútimo, etc. 
//Ejemplo: cambiaHaciaElCentro([true, 42, “Ada”, 2, “pizza”]) cambia el array a[“pizza¨, 42, “Ada”, true].
//cambiaHaciaElCentro([1,2,3,4,5,6]) cambia el array a [6,2,4,3,5,1]. No es necesario devolver (return) el array esta vez.

function intercambia(array) {
    for (let index = 0; index < array.length / 2; index++) {
        if (index % 2 == 0) {
            var num = array[array.length - (1 + index)];
            array[array.length - (1 + index)] = array[index]; 
            array[index] = num;
        }

    }
    return array;
}

console.log(intercambia([1, 2, 3, 4, 5, 6]));

//--14--
//Escala el Array - 
//Dado un array arr y un número num, 
//multiplica todos los valores en el array arr por el número num, y devuelve el array arr modificado. 
//Por ejemplo, escalaArray([1,2,3], 3) debería devolver [3,6,9].

function escalaArra(array, num) {
    for (let i = 0; i < array.length; i++) {
        array[i] = array[i] * num;
    }
    return array;
}
console.log(escalaArra([1, 2, 3], 3));
