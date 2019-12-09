from django.urls import path
from .views import *
app_name = 'app1'
urlpatterns =[
    path('',index,name='index'),
    path('yao/',index_y,name='index_y')
]