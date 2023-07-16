from django.urls import path
# подключаю свои представление
from .views import index, home, top_sellers, test1, test2
# urlpatterns - переменная в которой хранятся ссылки
# параметр name нужен для того чтобы использовать короткую команду для ссылки
urlpatterns = [
    path('',home, name = 'home'),
    path('top_sellers/',top_sellers, name='top_sellers'),
    path('index/',index),
    path('test1/',test1, name = 'test1'),
    path('test2/',test2, name = 'test2'),

]




# 1 - создать html в templates
# 2 - создать функцию-представление в views.py
# 3 - создать ссылку и указать в ней фунцию представление в urls.py









