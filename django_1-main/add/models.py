from django.db import models
from django.contrib import admin
from django.utils import timezone # Для времени
from django.utils.html import format_html # для создания строки html


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

    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    # для работы с самой таблицы
    class Meta:
        db_table = 'add' # название таблицы
    
    @admin.display(description='для создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date(): # проверяю, что запись была создана сегодня
            created_time = self.created_at.time().strftime('%H:%M:%S') #делаю в формате часы:минуты:секунды
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>', created_time
            )
        return self.created_at.time().strftime('%d.%m.%Y at %H:%M:%S')
    
    @admin.display(description='для обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date(): # проверяю, что запись была создана сегодня
            updated_time = self.updated_at.time().strftime('%H:%M:%S') #делаю в формате часы:минуты:секунды
            return format_html(
                '<span style = "color:green; font-weight:bold">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.time().strftime('%d.%m.%Y at %H:%M:%S')


# from add.models import Advertisement
# adv1 = Advertisement(title = 'Дошик', description = 'Дошик с помидором', price = 26, auction = True) # создал запись
# adv1.save() # сохранение записи

# Advertisement.objects.all()    

# from django.db import connection
# connection.queries # увидеть все запросы в sql

# exit()