from django.urls import include, re_path, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Profile
    re_path(r'^profile', views.profile, name='profile'),

    # Safety Portal
    re_path(r'^safety-portal', views.safety_portal, name='safety-portal'),

    # Checklist
    re_path(r'^checklist-filled', views.checklist_filled, name='checklist-filled'),

    # Checklist
    re_path(r'^checklists/(?P<pk>[0-9]+)/update', views.PropertyUpdateView.as_view(), name="update-checklist"),
    re_path(r'^checklists/new-checklist', views.PropertyCreateView.as_view(), name='new-checklist'),
    re_path(r'^checklists', views.PropertyListView.as_view(), name='checklist'),
    
    # Sign in
    re_path(r'^signin', views.signin, name='signin'),

    # Register
    re_path(r'^signup-success', views.signup_success, name='signup-success'),
    re_path(r'^signup', views.signup, name='signup'),

    # Home
    re_path(r'^home', views.home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)