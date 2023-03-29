from django.urls import include, re_path, path
from . import views

urlpatterns = [
    # Checklist
    re_path(r'^checklist', views.checklist, name='checklist'),
    
    # Register
    re_path(r'^signup-success', views.signup_success, name='signup-success'),
    re_path(r'^signup', views.signup, name='signup'),

    # Home
    re_path(r'^home', views.home, name='home'),
]