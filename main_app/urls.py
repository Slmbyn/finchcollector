from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allfinches/', views.allfinches, name='allfinches'),
    path('allfinches/<int:finch_id>/', views.finch_detail, name='detail'),
    path('allfinches/create', views.FinchCreate.as_view(), name='finches_create')
]