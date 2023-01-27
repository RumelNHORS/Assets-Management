from django import forms
from . models import AssetsModel, CheckIn, CheckOut

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = AssetsModel
        fields = ['id', 'date', 'name', 'phone', 'email', 'asset', 'brand', 'quantity']

        widgets = {
            'date': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'asset': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProductCheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['id', 'customer_name', 'email', 'phone', 'asset', 'checkin_date']
        
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'asset': forms.TextInput(attrs={'class':'form-control'}),
            'checkin_date': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class ProductCheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ['id', 'customer_name', 'email', 'phone', 'asset', 'checkout_date']
        
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'asset': forms.TextInput(attrs={'class':'form-control'}),
            'checkout_date': forms.TextInput(attrs={'class':'form-control'}),
        }
        
        