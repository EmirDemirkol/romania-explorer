from django.urls import path
from . import views

app_name = 'geography'

urlpatterns = [
    path('', views.GeographyView.as_view(), name='geography'),
    path('areas/', views.AreaListView.as_view(), name='area_list'),
    path('areas/<int:pk>/', views.AreaDetailView.as_view(), name='area_detail'),
    path('areas/create/', views.AreaCreateView.as_view(), name='area_create'),
    path('areas/<int:pk>/update/', views.AreaUpdateView.as_view(), name='area_update'),
    path('areas/<int:pk>/delete/', views.AreaDeleteView.as_view(), name='area_delete'),
    path('attractions/', views.AttractionListView.as_view(), name='attraction_list'),
    path('attractions/<int:pk>/', views.AttractionDetailView.as_view(), name='attraction_detail'),
    path('attractions/create/', views.AttractionCreateView.as_view(), name='attraction_create'),
    path('attractions/<int:pk>/update/', views.AttractionUpdateView.as_view(), name='attraction_update'),
    path('attractions/<int:pk>/delete/', views.AttractionDeleteView.as_view(), name='attraction_delete'),
]