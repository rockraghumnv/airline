from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('',views.flight_search,name='flight_search'),
    path('suggestions/',views.suggestions,name='suggestions'),
    path('book/',views.book,name='book'),
]