from .cart import Cart

# Create context processor to enable cart in all pages
def cart(request):
    return {"cart": Cart(request)}
