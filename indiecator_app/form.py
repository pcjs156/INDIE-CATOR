from django import forms
from django.shortcuts import render, get_object_or_404

from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'debut_date', 'member', 'description', 'profile_image']


# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = ['profile_image']
    
#     def __init__(self, *args, **kwargs) :
#         super(UploadImageForm, self).__init__(*args, **kwargs)
    
