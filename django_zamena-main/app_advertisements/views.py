from django.shortcuts import render,redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls

from django.core.handlers.wsgi import WSGIRequest

from .models import Advertisements
from .forms import AdvertisementForm


from django.contrib.auth.decorators import login_required # если пользователь не авторизован перенаправляем его
from django.urls import reverse_lazy # как reverse но только ленивая функция


# функция представление
def index(request):
    advertisiments =  Advertisements.objects.all() # все записи
    context = {'advertisiments': advertisiments}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")

@login_required(login_url=reverse_lazy('login'))
def post_adv(request: WSGIRequest):
    
    print('request.GET',request.GET)
    print('request.POST',request.POST)
    print('request.FILES',request.FILES)
    print('request.user',request.user)

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES) # передаю данные с запроса на проверку 
        if form.is_valid(): # True/False  проверяю правильность
            # print(request.POST['title'])
            print(form.cleaned_data) # отдает словарь со всеми данными
            adv = Advertisements(**form.cleaned_data) # распаковка словаря
            adv.user = request.user # отдельно указал пользователя 
            adv.save()  # сохраняю запись
            return redirect(
                reverse('home') # переадресация на главную страницу 
            )

        else: # если неправильно
            print(form.errors) # вывожу эту ошибку


    else: # GET или другие
        form = AdvertisementForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'advertisement-post.html', context)





def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')