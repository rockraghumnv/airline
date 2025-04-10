from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('/flights_list',views.flight_list,name='flight_list'),
    path('/flight_search',views.flight_search,name='flight_search'),
    path('/suggestions',views.suggestions,name='suggestions'),
    path('<int:flight_id>/book',views.book,name='book'),
    path('/success',views.success,name='success'),
    path('/login',views.login,name="login")
    path('<int:flight_id>/login_redirect',views.login_redirect,name='login_redirect')
]