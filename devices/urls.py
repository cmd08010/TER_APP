from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from devices import views

urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)