from django.conf.urls import url
from .views import all_cards


urlpatterns = [
    url(r"^all_cards", all_cards, name = "all_cards"),
    ]