class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get curent session key if it exist
        cart = self.session.get("session_key")

        # If logged user is new, create new session key
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make sure cart is available on all pages of sites
        self.cart = cart

    def add(self, product):
        productId = str(product.id)

        # Logic
        if productId in self.cart:
            pass
        else:
            self.cart[productId] = {"Price: ": str(product.price)}

        self.session.modified = True
