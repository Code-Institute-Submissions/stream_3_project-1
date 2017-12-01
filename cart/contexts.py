from django.shortcuts import get_object_or_404
from cards.models import Card


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page. 
    """

    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    card_count = 0
    for id, quantity in cart.items():
        card = get_object_or_404(Card, pk=id)
        total += quantity * card.price
        card_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'card': card})

    return { 'cart_items': cart_items, 'total': total, 'card_count': card_count }