from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from etender import settings
from . import models

class AdminsLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=models.Admins
        fields=('username','password')
        widgets={
             'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompanyLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=models.Companies
        fields=('username','password')
        widgets={
             'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompanyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=models.Companies
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TenderForm(forms.ModelForm):
    tender_close_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control datepicker','placeholder':'Date'}),input_formats=('%d/%m/%Y', ))
    class Meta:
        model=models.Tenders
        fields="__all__"
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'budget': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TenderApplyForm(forms.ModelForm):
    class Meta:
        model=models.TenderAppliers
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control'}),
            'bid_amount': forms.TextInput(attrs={'class': 'form-control'}),
        }