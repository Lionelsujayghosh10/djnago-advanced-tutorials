from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils.timezone import now



class Users(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=150, unique=True, null=False, blank=False)
    fname = models.CharField(max_length=100, default='schoolink')
    user_type = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(default=now)
    password = models.CharField(max_length=255)
    is_delete = models.PositiveSmallIntegerField(default=0)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['password']




    class Meta:
        db_table = "users"




