from django.urls import path
from main.views import home_page, gallery_page, pricing_page, about_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('gallery/', gallery_page, name='gallery'),
    path('gallery/<int:pk>/', gallery_page, name='detail'),
    path('pricing/', pricing_page, name='pricing'),
    path('about/', about_page, name='about')
]