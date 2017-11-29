from django.shortcuts import render
from .models import Card
from categories.models import Category

# Create your views here.
def all_cards(request):
    cards = Card.objects.all()
    return render(request, "cards.html", {"cards" : cards})
    
def all_cards_by_route_category(request):
    cards = Category.objects.filter(parent=None)
    # cards = Card.objects.filter(price__lte=50)
    return render(request, "categories.html", {"cards" : cards})
