from django.urls import path
from arkauth import views

urlpatterns=[
    path('signup/', views.signup, name='signup') 
]