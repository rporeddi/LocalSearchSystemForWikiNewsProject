from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import WikiNewsUser
from .import views
from .forms import NewUserForm, EditUserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import  Paginator, InvalidPage, EmptyPage, PageNotAnInteger


# View function for Login operation
def LoginView(request):
    if request.method=='POST':
        userdetails = UserLoginForm(request.POST)
        if userdetails.is_valid():
            username = userdetails.cleaned_data['username']
            user = WikiNewsUser.objects.filter(username=username)
            request.session['username'] = user[0].username
            admin = False
            for field in user:
                admin = field.is_admin
            if admin:
                return UserManagementView(request)
            else:
                return HttpResponseRedirect('/wikinews/userhome/')

        else:
            return render(request, "index.html", {'form': userdetails})
    else:
        form = UserLoginForm(None)
        return render(request, 'index.html', {'form': form})


# View function for User List page
def UserManagementView(request):
    userList = WikiNewsUser.objects.all()
    return render(request, 'user-management.html', {'data': userList})


# View function for New User form
def NewUserView(request):
    if request.method == 'POST':
        newuserdetails = NewUserForm(request.POST)
        if newuserdetails.is_valid():
            model = WikiNewsUser()
            model.username = newuserdetails.cleaned_data['username']
            model.password = newuserdetails.cleaned_data['password']
            model.is_admin = newuserdetails.cleaned_data['isadmin']
            print(newuserdetails.cleaned_data['isadmin'])
            model.save()
            return HttpResponseRedirect('/user/usermanagement')
        else:
            return render(request, 'newuser.html', {'form': newuserdetails})
    else:
        form = NewUserForm(None)
        return render(request, 'newuser.html', {'form': form})


# View function for Logout operation
def LogoutView(request):
    del request.session['username']
    return HttpResponseRedirect('/user/login')



# View function for Delete User operation
def DelUser(request,userId):
    user=WikiNewsUser.objects.get(id=userId)
    user.delete()
    return  HttpResponseRedirect('/user/usermanagement')



# View function for Edit User operation
def EditUser(request):
    form = EditUserForm(request.POST)
    if request.method=='POST':
        try:
            userId = form.data['edituserid']
            user = WikiNewsUser.objects.get(id=userId)
            user.username = form.data['editusername']
            user.password = form.data['editpassword']
            try:
                is_admin = request.POST['editisadmin']
            except MultiValueDictKeyError:
                is_admin = False
            if 'editisadmin' in form.data:
                user.is_admin = True
            else:
                user.is_admin = False

            user.save()
        except:
            return HttpResponseRedirect('/user/usermanagement')
    return HttpResponseRedirect('/user/usermanagement')


