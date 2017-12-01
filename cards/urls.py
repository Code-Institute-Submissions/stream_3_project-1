from django.conf.urls import url
from .views import all_cards, do_search


urlpatterns = [
    url(r"^all_cards", all_cards, name = "all_cards"),
    url(r"^search", do_search, name = "search"),
    ]