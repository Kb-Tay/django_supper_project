from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='base-home'),
    path('order/',views.order, name='base-order')
]