from django.urls import include, re_path, path
from . import views

urlpatterns = [
    # Checklist
    re_path(r'^checklists/new-checklist', views.PropertyCreateView.as_view(), name='new-checklist'),
    re_path(r'^checklists', views.checklists, name='checklist'),
    # Register
    re_path(r'^signup-success', views.signup_success, name='signup-success'),
    re_path(r'^signup', views.signup, name='signup'),

    # Home
    re_path(r'^home', views.home, name='home'),
]