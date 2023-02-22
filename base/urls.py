from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search),
    path('school/<str:pk>/', views.school, name='school'),
    path('school/<str:pk>/review', views.review, name='review')
]