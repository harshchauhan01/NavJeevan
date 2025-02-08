from django import forms
from .models import Patent
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class PatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        fields = ['patent_number', 'patent_title', 'patent_id','patent_age' ,'inventor_name', 'filing_date', 'patent_status', 'bed_allotted', 'bed_number', 'icu','photo','billing_date','address','patent_gender']




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

