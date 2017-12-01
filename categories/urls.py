from django.conf.urls import url
from .views import get_category
from .views import all_cards_by_occasion

urlpatterns = [
    url(r'^occasion/(\d+)$', all_cards_by_occasion, name='occasion'),
    url(r'^(?P<id>\d+)$', get_category, name='category'),
]