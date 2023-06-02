
from django.contrib import admin
from django.urls import path,include
from customer.views import *

urlpatterns = [
    path('get-customers',Getcustomerview.as_view()),

    


]
