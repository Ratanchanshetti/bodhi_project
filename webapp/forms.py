from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter ur name'}),label='Name',max_length=20,min_length=5,required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter ur e-mail'}),label='E-mail',max_length=40,min_length=5,required=True)
    number=forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter ur number'}),label='Number',max_length=10,min_length=10,required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),label='Subject',max_length=50,min_length=8,required=True)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}),label='Message',max_length=200,min_length=10,required=True)
