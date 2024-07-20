from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name ='home'),
    path('rate/<int:pk>/', views.rate_professor, name='rate'),
    path('ratings/',views.check_rating, name='check_rating'),
    path('overall_rating/<int:pk>/', views.overall_rating, name='overall_rating'),

    
]
