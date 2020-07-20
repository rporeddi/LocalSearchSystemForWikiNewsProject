from django.urls import path
from .import views


app_name = 'User'

urlpatterns = [
    path('login', views.LoginView),
    path('loginaction', views.UserView, name='loginaction'),
    path('login', views.LogoutView, name = "logout"),
    path('usermanagement', views.UserManagementView, name = "usermanagement"),
    path('Searchpage', views.SearchView, name = "searchpage"),

]