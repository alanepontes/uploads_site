from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import PostDocument

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class PostDocumentForm(forms.ModelForm):
    class Meta:
        model = PostDocument
        fields = ('title', 'resume','docfile')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control'}),
            'docfile': forms.FileInput(attrs={'class': 'form-control'})
        }
