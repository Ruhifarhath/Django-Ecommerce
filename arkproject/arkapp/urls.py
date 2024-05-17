
from django.urls import path
from arkapp import views

urlpatterns = [
    path('first/', views.first_view),
]
