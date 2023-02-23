from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

class AccountManager(BaseUserManager):
   def create_user(self, email, password, **extra_fields):
      if not email:
         raise ValueError(_("The Email must be set"))
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save()
      return user
   def create_superuser(self, email, password, **extra_fields):
      extra_fields.setdefault("is_staff", True)
      extra_fields.setdefault("is_superuser", True)
      extra_fields.setdefault("is_active", True)

      if extra_fields.get("is_staff") is not True:
         raise ValueError(_("Superuser must have is_staff=True."))
      if extra_fields.get("is_superuser") is not True:
         raise ValueError(_("Superuser must have is_superuser=True."))
      return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(_("Email"), max_length=254, unique=True)
   username = models.CharField(_("Username"), max_length=50, unique=True)
   first_name = models.CharField(_("First Name"), max_length=50)
   last_name  = models.CharField(_("Last Name"), max_length=50)
   phone_number = models.CharField(_("Phone Number"), max_length=20, unique=True)
   is_staff = models.BooleanField(_("is Staff"), default=False)
   is_active = models.BooleanField(_("is Active"), default=True)
   date_joined = models.DateField(_("Date Joined"), auto_now_add=True)
   
   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_number",]

   objects = AccountManager()

   class Meta:
      verbose_name = "account"
      verbose_name_plural = "accounts"
      
   def __str__(self):
       return self.email
   
   def get_full_name(self):
      return f"{self.first_name} {self.last_name}"
   