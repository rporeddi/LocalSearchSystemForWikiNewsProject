from django.urls import path, include
from .import views


app_name = 'User'

urlpatterns = [
    path('login', views.LoginView, name='loginview'),
    path('login', views.LogoutView, name = "logout"),
    path('usermanagement', views.UserManagementView, name = "usermanagement"),
    path('newuser', views.NewUserView),
    path('search/', include('haystack.urls')),
    path('del/<int:userId>',views.DelUser),
    path('ediuser',views.EditUser, name='edituser'),
]