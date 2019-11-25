from django import forms
from .models import Picture

class ImageForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
