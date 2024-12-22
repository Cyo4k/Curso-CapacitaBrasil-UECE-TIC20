

function adicionarItem() {
    let item = prompt("Digite o item: ");
    let carrinho = document.getElementById("carrinho");

    const itemCarrinho = document.createElement("li");
    itemCarrinho.innerHTML = item;
    carrinho.appendChild(itemCarrinho);
}