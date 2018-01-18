"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import get_index
from cards.views import all_cards
from accounts import urls as accounts_urls
from cards import urls as cards_urls
from categories import urls as categories_urls
from checkout import urls as checkout_urls
from cart import urls as carts_urls
from contact.views import contact
from .settings import MEDIA_ROOT
from django.views import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="index"),
    url(r"^accounts/", include(accounts_urls)),
    url(r"^cards/", include(cards_urls)),
    url(r'^categories/', include(categories_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^cart/', include(carts_urls)),
    url(r"^checkout/", include(checkout_urls)),
    url(r"^contact/", contact, name="contact"),
]
