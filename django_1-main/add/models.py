from django.db import models


#venv/Scripts/activate
# название цена описание дата создания/обновления   торг

# py manage.py makemigrations - создание файлов миграции
# py manage.py migrate - выполнение миграций (создание физических таблиц)

class Advertisement(models.Model):# наследую класс Model для создания таблицы в БД
    title = models.CharField('название',max_length=100) #  текстовое поле
    description = models.TextField("описание")
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Отметьте, возможен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)# сохраняем дату создания
    updated_at = models.DateTimeField(auto_now=True)# дата будет обновляться каждый раз при измении обьявления