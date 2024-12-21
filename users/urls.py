from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view')
]