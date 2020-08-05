from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #username, first_name, last_name, email, is_staff, is_active, date_joined
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
