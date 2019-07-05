from django import forms

from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username','first_name','last_name','email','password')
        widgets = {
            'username':forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),
            'first_name':forms.TextInput(attrs = {'class':'form-control'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control'}),
            'email':forms.EmailInput(attrs = {'class':'form-control'}),
        }