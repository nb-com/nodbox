from django import forms
from .models import  imagetopdf
from django.forms import ClearableFileInput, FileInput




class ImagePDF(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(ImagePDF, self).__init__(*args, **kwargs)
    
     class Meta:
        model = imagetopdf
        labels = {
            'images': 'Select Images',
        }
        fields = ['images']
        widgets = {
            'images': FileInput(attrs={
            'multiple': True,
            'id':'file-input',
            'onchange':'preview()',
            'accept':'image/*'}),
        }