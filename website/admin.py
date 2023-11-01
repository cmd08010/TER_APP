from django.contrib import admin
from django.utils.translation import gettext as _, gettext_lazy

from .models import Register


class MyAdminSite(admin.AdminSite):
    login_template = 'templates/admin/login.html'
    admin.AdminSite.site_header = 'NHEC Transactive Energy Rate Admin App'


admin.site.register(Register)