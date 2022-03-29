var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		
		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}
	})
}

function addCookieItem(productId, action){
	var itemQuantity = document.getElementById(`quantity-${productId}`)
	if (action == 'add'){
        cart[productId] = {'quantity': itemQuantity.value}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1
		if (cart[productId]['quantity'] <= 0){
			delete cart[productId];
		}
	}

    if(action == 'edit'){
        cart[productId] = {'quantity': parseInt(itemQuantity.innerHTML) + 1}
    }

	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()
}