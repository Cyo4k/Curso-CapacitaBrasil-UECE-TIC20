let objeto = {};
console.log(objeto);

objeto = {
    nome: "João",
    idade: 31,
    sexo: "Masculino"
}
console.log(objeto);


let myArray = [];
myArray[0] = "Galinha";
myArray[1] = "Vaca"; 
myArray[2] = "Baleia";
myArray.push("Tua Mãe");
console.log(myArray.length);



myArray.forEach(function(item){
    console.log(item.toUpperCase());
})