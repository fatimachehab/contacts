# mycontacts/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession', 'telnumber', 'email', 'gender','date_expired','date_joined']
