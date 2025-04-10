from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('login_redirect/',views.login_redirect,name="login_redirect"),
    path('register/',views.register_view,name="register_view")
]