from django import forms
from basicapp.models import Accounts

class FormName(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Accounts
        fields = '__all__'