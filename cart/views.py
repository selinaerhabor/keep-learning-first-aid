from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product


""" 
Items in cart render on cart.html page
"""
def view_cart(request):
    return render(request, "cart.html")


"""
Allows user to add a quantity of the specified product to the cart, by default
user can add quantity of 1
"""
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('sale'))


"""
Adjusts the quantity of the specified product to the specified amount
"""
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


"""
Empties all items in shopping cart
"""
def empty_cart(request):
    cart = request.session.delete()
    return redirect(reverse('view_cart'), {"cart": cart})
    