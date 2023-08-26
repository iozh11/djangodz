from django.shortcuts import render
# импортируем классы для ответа
from django.http import HttpResponse


# функцию-представление
def lesson_4(request):
    return HttpResponse("ДЗ")
