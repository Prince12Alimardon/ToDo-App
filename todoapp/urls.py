from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', single, name='single'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),

]
