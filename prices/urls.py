from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from prices import views

urlpatterns = [
    path('prices/', views.PricesList.as_view()),
    path('prices/<int:pk>/', views.PricesDetail.as_view()),
    path('prices/today/', views.PricesLatest.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)