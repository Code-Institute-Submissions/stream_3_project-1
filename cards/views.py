from django.shortcuts import render
from .models import Card

# Create your views here.
def all_cards(request):
    cards = Card.objects.all()
    return render(request, "cards.html", {"cards" : cards})
    
def do_search(request):
    cards = Card.objects.filter(name__icontains=request.GET["q"])
    return render(request, "cards.html", { "cards" : cards })
