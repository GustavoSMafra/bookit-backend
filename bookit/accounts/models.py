from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, cpf=None, is_provider=False, is_staff=False, is_superuser=False):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_provider=is_provider,
            is_staff=is_staff,
            is_superuser=is_superuser,
            cpf=cpf,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, cpf=None, is_provider=False):
        user = self.create_user(
            email,
            first_name,
            last_name,
            cpf=cpf,
            password=password,
            is_provider=is_provider,
            is_staff=True,
            is_superuser=True,
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_provider = models.BooleanField()
    is_staff = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', "is_provider", "cpf"]

    objects = UserManager()

    # Alterações para resolver os erros de ambiguidade de acesso reverso
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        blank=True,
    )

    def __str__(self):
        return self.email
