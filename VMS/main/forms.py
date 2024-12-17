from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'contact', 'email', 'address', 'purpose', 'status', 'img']  # Include 'img' field

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter visitor name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address', 'rows': 3}),
            'purpose': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter purpose of visit', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'img/*'}),  # File input for img
        }

        labels = {
            'name': 'Visitor Name',
            'contact': 'Contact Number',
            'email': 'Email Address',
            'address': 'Address',
            'purpose': 'Purpose of Visit',
            'status': 'Status (IN/OUT)',
            'img': 'Upload img',  # Label for img field
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact.isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")
        if len(contact) > 15:
            raise forms.ValidationError("Contact number must not exceed 15 digits.")
        return contact
