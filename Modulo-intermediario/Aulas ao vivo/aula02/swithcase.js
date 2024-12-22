let altura = parseFloat(prompt("Digite sua altura: "));
let peso = parseFloat(prompt("Digite seu peso: "));


let imc = peso / (altura*altura)

console.log(imc);

switch (true) {
    case (imc < 22):
        console.log("Abaixo do peso");
        break;
    case (imc >= 22 && imc < 27):
        console.log("Peso ideal");
        break;
    case (imc >= 27 && imc < 30):
        console.log("Sobrepeso");
        break;
    case (imc >= 30 && imc < 40):
        console.log("Obesidade");
        break;
    default:
        console.log("Obesidade Grave");
    
}