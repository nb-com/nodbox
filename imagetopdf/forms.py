from django import forms
from .models import  imagetopdf
from django.forms import ClearableFileInput


class ImagePDF(forms.ModelForm):
    class Meta:
        model = imagetopdf
        fields = ['images']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }