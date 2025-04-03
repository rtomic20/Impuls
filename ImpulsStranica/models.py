from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
import os

def validate_word_file(file):
    ext = os.path.splitext(file.name)[1]  # npr. '.docx'
    valid_extensions = ['.doc', '.docx']
    if ext.lower() not in valid_extensions:
        raise ValidationError("Dozvoljeni su samo Word fajlovi (.doc ili .docx).")

def upload_to_user(instance, filename):
    return f"uploads/{instance.user.username}/{filename}"
# Admin
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, user_type="korisnik", **extra_fields):
        if not username:
            raise ValueError("Korisničko ime je obavezno.")
        user = self.model(username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

# Korinsik
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('korisnik', 'Korisnik'),
    )

    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='korisnik')
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.user_type == 'admin'

    def is_regular_user(self):
        return self.user_type == 'korisnik'

def upload_to_user(instance, filename):
    return f"{instance.user.username}/{filename}"

class Work(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_to_user, validators=[validate_word_file])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
