from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CateForm(ModelForm):
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    descript = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    status = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input mb-2', 'placeholder': ''}))
    trending = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input mb-2', 'placeholder': ''}))
    class Meta:
        model = Category
        fields = '__all__'


class ProdForm(ModelForm):
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    small_descript = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    original_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    selling_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    status = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input mb-2', 'placeholder': ''}))
    trending = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input mb-2', 'placeholder': ''}))
    descript = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    product_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    product_image1 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-2 ', 'placeholder': ''}))
    product_image2 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    product_image3 = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-2', 'placeholder': ''}))
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tag': forms.Select(attrs={'class': 'form-select'}),
        }




class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Confirm password'}))
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']