from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from store.models import Product


def cartSummary(request):
    return render(request, "pages/cartSummary.html", {})


def cartAdd(request):
    # Get cart
    cart = Cart(request)
    # Test POST
    if request.POST.get("action") == "POST":
        # Get it response
        productId = int(request.POST.get("productId"))
        # Look product in DB
        product = get_object_or_404(Product, id=productId)
        # Add to session
        cart.add(product=product)
        # Get cart quantity
        cartQuantity = cart.__len__()
        # Return response
        #response = JsonResponse({"Product name: ": product.name})
        response = JsonResponse({"Quantity: ": cartQuantity})
    return response


def cartDelete(request):
    pass


def cartUpdate(request):
    pass
