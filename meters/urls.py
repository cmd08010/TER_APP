from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from meters import views

urlpatterns = [
    path('meters/', views.MetersList.as_view()),
    path('meters/<int:pk>/', views.MetersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)