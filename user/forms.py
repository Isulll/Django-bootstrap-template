from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Username'}))
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Password'}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Password'}))
    