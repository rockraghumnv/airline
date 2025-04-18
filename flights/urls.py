from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('',views.flight_search,name='flight_search'),
    path('suggestions/',views.suggestions,name='suggestions'),
    path('book/',views.book,name='book'),
    path('store_flight_id/', views.store_flight_id, name='store_flight_id')
]