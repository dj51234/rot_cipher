from django.urls import path 
from . import views

urlpatterns = [
    path('', views.render_index, name='index'),
    path('result/',views.result,name='result')
]