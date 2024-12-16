from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-visitor/', views.register_visitor, name='add_visitor'),
    path('visitor-list/', views.visitor_logs, name='visitor_list'),
]
