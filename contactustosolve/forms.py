from django import forms
from django.forms.models import ModelForm
from contactustosolve.models import Customer, Provider

class CustomerForm(ModelForm):
    customerName = forms.CharField(label='Ügyfél neve')
    customerPhone = forms.CharField(label='Ügyfél telefonszáma' , widget = forms.TextInput(attrs={"placeholder": "70/123-4567"}))
    customerEmail = forms.CharField(label='Ügyfél e-mail címe', widget = forms.TextInput(attrs={"placeholder": "minta@valami.hu"}), required=None)
    class Meta:
        model = Customer
        
        fields = ['customerName', 'customerPhone', 'customerEmail']

class ProviderForm(ModelForm):

    class Meta:
        model = Provider
        fields = ['providerName', 'night', 'rating', 'contactName', 'city', 'address', 'phoneNumber', 'email', 'activity',
                  'monOp', 'monCl', 'tueOp', 'tueCl', 'wedOp', 'wedCl', 'thuOp', 'thuCl', 'friOp', 'friCl', 'satOp', 'satCl', 'sunOp', 'sunCl']
