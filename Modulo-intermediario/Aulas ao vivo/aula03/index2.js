function addCarrinho(item) {
  const cartItems = document.getElementById("cart-items");
  const list = document.createElement("li");
  list.textContent = item;
  cartItems.appendChild(list);
}
