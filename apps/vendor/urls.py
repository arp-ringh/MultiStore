from django.urls import path
from django.contrib.auth import views as auth_views
#from .views import *
from . import views

app_name = "vendor"

urlpatterns = [
    path('vendor-apply/', views.vendor_apply, name='vendor-apply'),
    path('vendor-login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),

    ]

