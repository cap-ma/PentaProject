from django import forms
from .models import News

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image']

        