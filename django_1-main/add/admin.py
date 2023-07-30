from django.contrib import admin
from .models import Advertisement
# импорирую класс для подсказок
from django.db.models.query import QuerySet


# admin_class - класс для кастомизации

class AdvertisementAdmin(admin.ModelAdmin):
    # отображение в виде таблицы
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at']
    # параметры фильтрации
    list_filter = ['auction', 'created_at']

    # добавляю функции для выбранных хаписей
    actions = ['make_auction_as_false']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset:QuerySet):
        queryset.update(auctoin = False)


admin.site.register(Advertisement, AdvertisementAdmin) # подключаем модель
# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )