from django.shortcuts import render, redirect, reverse

# Cart contents render on page
def view_cart(request):
    return render(request, "cart.html")

# Adds a quantity of the specified product to the cart
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('sale'))


# Adjusts the quantity of the specified product to the specified amount
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
