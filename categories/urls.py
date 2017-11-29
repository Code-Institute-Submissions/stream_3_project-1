from django.conf.urls import url
from .views import get_category
from cards.views import all_cards_by_route_category

urlpatterns = [
    url(r'^$', all_cards_by_route_category, name='categories'),
    url(r'^(?P<id>\d+)$', get_category, name='category'),
]