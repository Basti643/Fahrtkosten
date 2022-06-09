from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from tankenapp.models import geolocation_test


class User_Form(UserCreationForm):
    e_mail = forms.CharField(max_length=30, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*E-Mail Adresse eingeben..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Passwort eingeben..','class':'password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Passwort bestätigen..','class':'password'}))


class AuthForm(AuthenticationForm):
	'''
	Form that uses built-in AuthenticationForm to handel user auth
	'''
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*E-Mail Adresse eingeben ..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Passwort eingeben..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )

# Custome Form vererbt von (UserCreationForm)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        localized_fields=('__all__',)
        
    # Felder und Attribute überschreiben z.B. Englishe Übersetzung der Form Namen 
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Benutzernamen eingeben...'})
        self.fields['username'].label = 'Benutzer'
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Passwort eingeben...'})
        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Passwort bestätigen...'})
        self.fields['password2'].label = 'Passwort bestätigen'
        






#class geolocForm (forms.ModelForm):
    # geolocation Test aus Models.py ?
    #address_input = forms.CharField(max_length=128, help_text="Bitte Standort eingeben.")

     # An inline class to provide additional information on the form.
    #class Meta:
        # Provide an association between the ModelForm and a model
        #model = geolocation_test
