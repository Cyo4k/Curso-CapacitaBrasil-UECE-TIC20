console.log("10" + 20);

let listaCompras = ["Leite", "Pão", "Suco"];

//Métodos de array

listaCompras.push("Café", "Ovo", "Farinha");
listaCompras.pop();


console.log("\n"+ "exemplo com forEach")
for(i=0;i< listaCompras.length; i++) {
  console.log(listaCompras[i]);
};

console.log("\n"+ "exemplo com forEach")


listaCompras.forEach(function(item){
  
  console.log(item);
})

//Arrow Functions

//Funcão tradicional
function dobro(n){
  return n*2;
}

//Arrow function
const dobro2 = n => n*2;

//Chamada das funções

console.log(dobro(4));
console.log(dobro2(4));

let numeros = [1,2,3,4,5,6,7,8,9,10];
let dobrados = numeros.map(n => n*2);
console.log(dobrados);

//Template Literals
let nome = "João";
let mensagem = `Olá ${nome}!, tudo bem?`;
console.log(mensagem);


//