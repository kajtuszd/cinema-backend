from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    phone = models.CharField(unique=True, null=True,
                             max_length=15, validators=[
                             RegexValidator(r'^\+?1?\d{9,15}$')])
    is_customer = models.BooleanField(default=True)
    is_worker = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
