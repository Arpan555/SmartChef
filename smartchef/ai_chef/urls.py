from django.urls import path
from ai_chef import views

urlpatterns=[
    path('',views.Home.as_view(),name='home')
]