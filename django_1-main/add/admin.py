from django.contrib import admin
from .models import Advertisement
# импорирую класс для подсказок
from django.db.models.query import QuerySet


# admin_class - класс для кастомизации

class AdvertisementAdmin(admin.ModelAdmin):
    # отображение в виде таблицы
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at', 'created_date', 'updated_date']
    # параметры фильтрации
    list_filter = ['auction', 'created_at']

    # добавляю функции для выбранных хаписей
    actions = ['make_auction_as_false']

    # создание блоков
    fieldsets = (
        (# 1 блок
            'Общее',{ # название блока
                'fields':('title', 'description') # поля блока
            }
        ),
        (# 1 блок
            'Финансы',{ # название блока
                'fields':('price', 'auction'), # поля блока
                'classes':['collapse'], # функционал для срытия блока
                'description':'Блок финансов' # Подсказка о блоке
            }
        )
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)


admin.site.register(Advertisement, AdvertisementAdmin) # подключаем модель
# py manage.py createsuperuser - создание аккаунта админа
# (вводин имя почту и пароль   ! пароль не отображается )