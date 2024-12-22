let carrinho = [];

const addCarrinho = (nome, preco) => {
    const itemIndex = carrinho.findIndex(item => item.nome === nome);
    if (itemIndex > -1) {
        carrinho[itemIndex].quantidade += 1;
    } else {
        carrinho.push({ nome, preco, quantidade: 1 });
    }
    atulizarCarrinho();
};

const atulizarCarrinho = () => {
    const cartItems = document.getElementById('itemsCarrinho');
    const totalItems = document.getElementById('total');
    cartItems.innerHTML = '';
    let total = 0;

    carrinho.forEach((item) => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.nome} - Quantidade: ${item.quantidade} - R$ ${item.preco * item.quantidade}`;
        cartItems.appendChild(listItem);
        total += item.preco * item.quantidade;
    });

    totalItems.textContent = total.toFixed(2);
};
