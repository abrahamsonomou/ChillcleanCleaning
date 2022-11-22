from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','sujet','message']
        labels={'nom':'Full Name','email':'Email Address','sujet':'Sujet','message':'Message'}
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control','placeholder':"Nom",'required':'required',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Email",'required':'required',}),
            'sujet':forms.TextInput(attrs={'class':'form-control','placeholder':"Sujet",'required':'required',}),
            'message':forms.Textarea(attrs={'class':'form-control','cols':30,'rows':10,'placeholder':"Message",'required':'required',})
        }
        
        