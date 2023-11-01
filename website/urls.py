"""blog_ter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('website/', include('website.urls'))
"""
from django.urls import path
from website import views
from .views import SearchDeviceView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_create_view),
    path('register_success/', views.register_success_view, name="register_success"),
    path('submissions/', views.register_list_view, name="submissions"),
    path('submission/<int:pk>/edit', views.submission_detail_view, name="submission_detail"),
    path('lookup/', SearchDeviceView.as_view(), name="lookup"),
]
