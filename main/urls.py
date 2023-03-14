from django.urls import include, re_path, path
from . import views

urlpatterns = [
    # Checklist
    re_path(r'^checklist', views.checklist, name='checklist'),
    
    # Home
    re_path('', views.home, name='home'),
    

]