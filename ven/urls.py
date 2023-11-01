from django.urls import include, path
from ven import views

urlpatterns = [
    path('ven/<ven_token>/', views.VenDetail.as_view())
]