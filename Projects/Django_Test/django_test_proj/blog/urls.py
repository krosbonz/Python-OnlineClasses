from django.urls import path
from . import views
# Import views.py from the current directory

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
# This is the homepage determined by the ''
# Gets its logic from views.py in the same directory
# Designate a name for the path