from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    email = forms.EmailField('Email')
    subject = forms.CharField(
        label='Subject',
        max_length=100,
    )
    message = forms.CharField(widget=forms.Textarea)

