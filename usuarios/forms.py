# from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Usuario
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# class UserForm(forms.Form):
#     name= forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}
#     ))
#     email= forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'Escriba su email'}
#     ))
#     password= forms.CharField(label="Password",required=True,widget=forms.PasswordInput(
#         attrs={'class': 'form-control','placeholder': 'Escriba su contraseña'}
#     ))

class UserForm(ModelForm):
    class Meta:
        model= Usuario
        fields = ['name','email','password']
        widgets= {
            'name': forms.TextInput( 
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba su nombre'
                }
            ),
            'email': forms.EmailInput( 
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba su correo'
                }
            ),
            'password': forms.PasswordInput( 
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escriba su contraseña'
                }
            )

        }

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args ,**kwargs)
        self.fields['email'].widget.attrs['class'] ='form-control'
        self.fields['email'].widget.attrs['placeholder'] ='Escriba su email'
        self.fields['password'].widget.attrs['class'] ='form-control'
        self.fields['password'].widget.attrs['placeholder'] ='Escriba su contraseña'

        