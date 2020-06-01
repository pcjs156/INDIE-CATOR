from django import forms
from django.shortcuts import render

from .models import Artist

class DateInput(forms.DateInput):
    input_type = 'date'

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'debut_date', 'member', 'description', 'profile_image']
        widgets = {
            'debut_date':DateInput(),
        }
class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )