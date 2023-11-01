from django.urls import include, path
from .views import UserCreateView, UserEditView, UserChangePasswordView, LogoutView
from accounts import views

urlpatterns = [
    path('admin/settings', views.admin_settings_view, name='admin_settings'),
    path('change_password', UserChangePasswordView.as_view(), name='change_password'),
    path('user/add', UserCreateView.as_view(), name='add_user'),
    path('user/<int:pk>/edit', UserEditView.as_view(), name="edit_user"),
    path('user/<int:pk>/delete', views.delete_user, name="delete_user"),
    path('logout', LogoutView.as_view(), name="logout_user"),
    path('settings/', views.settings_view, name="settings"),
    path('account', include('django.contrib.auth.urls')),
]