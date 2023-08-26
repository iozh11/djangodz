"""advertisements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# импортировать представления ДЗ
from lesson_4.views import lesson_4

# 
from django.conf import settings # настройки
from django.conf.urls.static import static # функцмия для создания автоматических ссылок


urlpatterns = [
    path('admin/', admin.site.urls), # ссылка для панели админа
    path('lesson_4/',lesson_4),
    path('', include('app_advertisements.urls')),
    path('auth/', include('app_auth.urls')),

]


if settings.DEBUG: # если дебаггинг включен
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # подключаю ссылки медиа файлов














