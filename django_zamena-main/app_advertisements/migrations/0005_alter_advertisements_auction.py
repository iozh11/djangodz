# Generated by Django 3.2.20 on 2023-07-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_advertisements_auction_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='auction',
            field=models.BooleanField(default=False, help_text='Возможен торг или нет', verbose_name='торг'),
        ),
    ]
