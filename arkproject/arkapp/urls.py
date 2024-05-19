
from django.urls import path
from arkapp import views

urlpatterns = [
    path('home/', views.first_view),
]
