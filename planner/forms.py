from django.forms import ModelForm, widgets
from django import forms
from .models import *
from django.forms.widgets import SelectDateWidget


# class PlantripForm(forms.ModelForm):
#     class Meta:
#         model = Plantrip
#         fields = '__all__'
        



# forms.py


# class PlantripForm(forms.ModelForm):
#     class Meta:
#         model = Plantrip
#         fields = ['departure', 'destination', 'startdate', 'enddate', 'starttime', 'endtime', 'grouptrip', 'solotrip']




# class RentForm(forms.ModelForm):
#     class Meta:
#         model = Rent
#         fields = '__all__'
#         widgets = {
#             'house_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
#             'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 500px'}),
#             'area': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
#             'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
#         }
