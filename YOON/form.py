from django import forms
from .models import Blog,Guest

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['title', 'body']