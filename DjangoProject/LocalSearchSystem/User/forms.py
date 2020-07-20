from django.forms import ModelForm
from django import  forms
from .models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean(self):
        data = User.objects.all()
        super(LoginForm, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        for item in data:
            if username != item.username:
                self._errors['username'] = self.error_class([
                    'Invalid username'])
            elif password != item.password:
                self._errors['password'] = self.error_class([
                    'Invalid password'])
            else:
                break


        return self.cleaned_data
