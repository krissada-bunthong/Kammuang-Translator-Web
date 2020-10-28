from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result',views.result,name='result'),
    path('tokenize',views.tokenize,name='tokenize'),
    path('read_csv',views.read_csv,name='read_csv'),
]