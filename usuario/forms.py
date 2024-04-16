from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Informe um email válido')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ExtendedCadastroForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Informe um email válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso. Por favor, escolha outro.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', "Este email já está em uso. Por favor, escolha outro.")
        return cleaned_data
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['username'].label = 'username'
    class Meta:
        model = User
        fields = ['username', 'password']