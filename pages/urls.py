from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('references/', views.page_detail, {'slug': 'references'}, name='references'),
    path('pages/<slug:slug>/', views.page_detail, name='page_detail'),
]
