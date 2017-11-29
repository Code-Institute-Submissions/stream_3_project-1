from django.shortcuts import render, get_object_or_404
from .models import Category
from cards.models import Card

# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)
    # cards = Card.objects.filter(price__lte=50)

    args = { 'categories': categories, 'subcategories': {}, 'cards': {}}
    return render(request, 'categories.html', args)


def get_category(request, id):
    this_category = get_object_or_404(Category, pk=id)
    #root_categories = Category.objects.filter(parent=None)

    crumbs = []
    crumb = this_category
    while crumb != None:
        crumbs.insert(0, crumb)
        crumb = crumb.parent

    subcategories = Category.objects.filter(parent=this_category)

    cards = this_category.cards.all()

    args = { 'categories': subcategories, 'cards': cards, 'crumbs': crumbs}
    return render(request, 'categories.html', args)


def root_categories_context(request):
    categories = Category.objects.filter(parent=None)

    category_tree = {}

    for category in categories:
        sub_categories = Category.objects.filter(parent=category)
        category_tree[category] = sub_categories

    return {'root_categories': category_tree}