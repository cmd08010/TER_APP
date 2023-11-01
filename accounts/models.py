from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django import forms

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    # email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.',
                                   verbose_name='staff status')
    permission_type = models.CharField(max_length=250)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.permission_type and self.permission_type == "admin":
            self.is_superuser = False
        else:
            self.is_superuser = True
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username