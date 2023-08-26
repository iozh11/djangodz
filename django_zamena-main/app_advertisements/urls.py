# маршрутизатор приложения
from django.urls import path

from .views import index, top_sellers ,post_adv



urlpatterns = [
    path('', index, name='home'),

    path("post_adv/", post_adv, name='post_adv'), # топ продавцов 

    path('top_sellers', top_sellers, name='top_sellers'),


]


 