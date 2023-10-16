from django import forms
from .models import *

from .models import GalleryImage
  
class HotelForm(forms.ModelForm):
  
    class Meta:
        
        fields = ['name', 'Foto_clinic']

# GalleryImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadImageForm(forms.ModelForm):
    images = MultipleFileField(widget=MultipleFileInput())

    class Meta:
        model = GalleryImage
        fields = ('images',)


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)    
    subject = forms.CharField(label='Сотовый', required=True)    
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)

