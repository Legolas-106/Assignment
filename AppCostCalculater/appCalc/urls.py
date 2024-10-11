from django.urls import path
from appCalc.views import *
urlpatterns = [
    path('',homePage,name='Home_Page'),
    path('get_cost',get_cost,name="get_cost")
]
