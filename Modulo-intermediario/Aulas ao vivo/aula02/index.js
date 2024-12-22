let nome = prompt("Digite seu nome: ");

let nota1 = parseFloat(prompt("Digite a primeira nota: "));
let nota2 = parseFloat(prompt("Digite a segunda nota: "));

let media = (nota1 + nota2) / 2;

window.alert(`O aluno ${nome} tirou ${nota1} e ${nota2} e tirou a media de ${media}`);