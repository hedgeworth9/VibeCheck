from django.urls import include, re_path, path
from . import views

urlpatterns = [
    # Profile
    re_path(r'^profile', views.profile, name='profile'),

    # Safety Portal
    re_path(r'^safety-portal', views.safety_portal, name='safety-portal'),

    # Checklist
    re_path(r'^checklist-filled', views.checklist_filled, name='checklist-filled'),

    # Checklist
    re_path(r'^checklists/new-checklist', views.PropertyCreateView.as_view(), name='new-checklist'),
    re_path(r'^checklists', views.checklists, name='checklist'),
    
    # Sign in
    re_path(r'^signin', views.signin, name='signin'),

    # Register
    re_path(r'^signup-success', views.signup_success, name='signup-success'),
    re_path(r'^signup', views.signup, name='signup'),

    # Home
    re_path(r'^home', views.home, name='home'),
]