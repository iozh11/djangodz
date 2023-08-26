from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Advertisements



from django.core.exceptions import ValidationError 

# class AdvertisementForm(forms.Form):
#     # class="row mb-3 offset-sm-4"
#     title       = forms.CharField(max_length=100, widget=forms.TextInput(
#         {"class": "form-control-lg"}
#     )) 
#     description = forms.CharField(widget=forms.Textarea(
#         {"class": "form-control-lg"}
#     ))
#     price       = forms.DecimalField(widget=forms.NumberInput(
#         {"class": "form-control-lg"}
#     ))
#     auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
#         {"class": "form-check-input"}
#     )) # поле необязательное
#     image       = forms.ImageField(widget=forms.FileInput(
#         {"class": "form-control-lg"}
#     ))


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #1 дз
        # print(self.fields)
        self.fields['title'].widget.attrs['class'] = "form-control-lg"
        self.fields['description'].widget.attrs['class'] = "form-control-lg"
        self.fields['price'].widget.attrs['class'] = "form-control-lg"
        self.fields['auction'].widget.attrs['class'] = "form-check-input"
        self.fields['image'].widget.attrs['class'] = "form-control-lg"




    class Meta:
        model = Advertisements
        fields = ['title','description','price','auction','image']


    #2дз 
    def clean_title(self):
        title = self.cleaned_data['title'] # извлек название из данных пользователя
        if title.startswith('?'):# проверяю что начинеается с ?
            raise ValidationError("Название не может начинаться с ?")
        return title    # если не ? то возвращаю title обратно
