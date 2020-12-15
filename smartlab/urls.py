from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notification/', views.notification, name='notification'),
    path('stastics/', views.stastics, name='stastics'),

]