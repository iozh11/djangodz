from django.shortcuts import render
# полуяает запросы и отдает ответы

# подключаю классы
from django.http import HttpResponse # для ответа

def index(request):
    return HttpResponse("Привет")# возвращаю ответ



# функция-представление
# render - функция которая по запросу возвращение html 
def home(request):
    return render(request, 'index.html')


def top_sellers(request):
    return render(request, 'top-sellers.html')

# создаю функции представления
def test1(request):
    return render(request, 'test1.html')


def test2(request):
    return render(request, 'test2.html')