from django.urls import path
from CalculatorApp import views
urlpatterns = [
    path('home/',views.home,name='home'),
]