//1.-Configura un array para que los valores negativos se transformen en 0. 
//Por ejemplo, resetNegativos([1, 2, -1, -3]) debiera dar como resultado[1, 2, 0, 0].
function moverAdelante(array){
    ade=[];
    for (var i = 0; i < array.length; i++){
        (array[0]<array.length-1);{
            ade.push(array.length);
        }
        
        //
    }    
        return array;

}
x = moverAdelante([1,2,3]);
console.log(ade);


//2.-Dado un array, mueve todos los valores un espacio de derecha a izquierda eliminando el primer valor y dejando un 0 para el último valor. 
//Por ejemplo, moverAdelante([1,2,3]) debiera dar como resultado [2,3,0].

function moverAdelante(array){
    ade=[];
    for (var i = 1; i < array.length; i++){
        (array[0] >= 1); {
            ade.push(array[i]);

        }

        
        
    }   
        ade.push(0);
        return array;
}
x = moverAdelante([1,2,3]);
console.log(ade);

//3.-Configura un array para que el resultado sean los valores en el orden contrario. 
//Por ejemplo, returnReverso([1,2,3]) debe dar [3,2,1].

function returnReverso(arr){
    ret=[];
    for( var i=arr.length-1;i>=0;i--){
        ret.push(arr[i]);
    }
    return arr;

}
x=returnReverso([1,2,3]);
console.log(ret);


//4.-Crea una función que cambie un array repitiendo sus valores originales (manteniendo el mismo orden).
//Por ejemplo, repetirValores([4, ”Ulysses”, 42, false]) debiera dar[4, 4, “Ulysses”, “Ulysses”, 42, 42, false, false].

function repetirValores(array){
    val=[];
    for(var i=0;i<arr.length;i++){
        val.push(array[i]);
        val.push(array[i]);
    }
    return array;
}
x=repetirValores([4, "Ulysses", 42, false]);
console.log(val);
