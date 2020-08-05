from django.forms import ModelForm
from django import  forms
from .models import  WikiNewsUser


class NewUserForm(forms.Form):
    username = forms.CharField(label='User Name' ,max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), max_length=100, label='Confirm Password')
    isadmin = forms.BooleanField(label='Admin' ,initial=True, required=False)

    def clean(self):
        super(NewUserForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data['password2']
        user = WikiNewsUser.objects.filter(username=username)
        print(len(user))
        print(user)
        if len(user) > 0:
            self._errors['username'] = self.error_class(['This User name is already taken'])
        elif password and len(password) < 8:
                self._errors['password'] = self.error_class(['Password should contain atleast 8 characters'])
        elif password and password2 and password != password2:
                self._errors['password2'] = self.error_class(['Password and Confirm Password do not match'])
        else:
            return self.cleaned_data


class EditUserForm(forms.Form):
    edituserid = forms.IntegerField(label='edituserid')
    editusername = forms.CharField(label='editusername' ,max_length=255)
    editpassword = forms.CharField(widget=forms.PasswordInput(), max_length=100)
    editisadmin = forms.BooleanField(label='editisadmin')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='User Name',max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=100,required=True)

    def clean(self):
        super(UserLoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = WikiNewsUser.objects.filter(username=username, password=password)
        database_password =""
        for item in user:
            database_password = item.password
        # print(user.password)
        if len(user) == 0:
            self._errors['username'] = self.error_class(['Invalid username'])
            self._errors['password'] = self.error_class(['Invalid password'])
        elif password != database_password:
            self._errors['password'] = self.error_class(['Invalid password'])
        else:
            return self.cleaned_data

