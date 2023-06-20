from django import forms

class UploadForm(forms.Form):
    user_image = forms.ImageField()