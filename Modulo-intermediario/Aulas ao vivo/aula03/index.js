let cabecalho = document.getElementById("cabecalho");

console.log(cabecalho);


function alterarCabecalho() {
    cabecalho.innerHTML = "Ola, bem vindo ao meu site!";
    cabecalho.style.color = "red";
    cabecalho.style.backgroundColor = "black";
    cabecalho.style.textAlign = "center";
    cabecalho.style.fontSize = "50px";
}