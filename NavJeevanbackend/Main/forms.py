from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class PatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        fields = ['patent_number', 'patent_title', 'patent_id','patent_age' ,'inventor_name', 'filing_date', 'patent_status', 'bed_allotted', 'bed_number', 'icu','photo','billing_date','address','patent_gender']


class MedForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_name', 'medicine_category', 'medicine_Avail']

class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = ['blood_group', 'blood_Avail', 'blood_donars']

class OrganForm(forms.ModelForm):
    class Meta:
        model = Organ
        fields = ['organ_name', 'organ_Avail', 'organ_donars']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class PrescriptionForm(forms.ModelForm):
    billing_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Prescription
        fields = ['patient_id', 'billing_date', 'total_fee']