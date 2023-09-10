from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .choices import *
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import random
from django.contrib import messages 


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Not SuperUser!")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Not SuperUser!")

        return self.create_user(email, password, **extra_fields)



class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=True, max_length=200, default='')
    last_name = models.CharField(blank=True, max_length=200)
    email = models.EmailField(blank=True, default='', unique=True)
    gender = models.CharField(max_length = 6, choices = genders)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    gov_id_prefix = models.CharField(max_length=3, choices = prefix)
    gov_id_number = models.CharField(max_length=8)  
    client_code = models.CharField(max_length=6, null=True, blank=True)
    birthdate = models.DateField(null=True, default=None)


    pin = models.CharField(
        max_length=7,
        default='',
        validators=[
            RegexValidator(
                regex=r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7}$',
                message="Invalid pin")])

      
    phone_number = models.CharField(
    max_length = 7, 
    validators = [
            RegexValidator(
        regex=r'^\d{7}$',
        message="Invalid number")])
    
    def clean(self):
        if self.gov_id_prefix == 'AA' and len(self.gov_id_number) != 7:
            raise ValidationError('For AA prefix, gov_id_number should have 7 digits.')
        if self.gov_id_prefix == 'AZE' and len(self.gov_id_number) != 8:
            raise ValidationError('For AZE prefix, gov_id_number should have 8 digits.')
        if (self.gov_id_prefix == 'MYI' or self.gov_id_prefix == "DYI") and len(self.gov_id_number) != 6:
            raise ValidationError('For MYI, DYI prefixes, gov_id_number should have 6 digits.')

    
    def save(self, *args, **kwargs):
        if not self.client_code:
            random_numbers = random.randint(0, 999999)
            self.client_code = f"{random_numbers:06d}"
        super().save(*args, **kwargs)


    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2, default=300.00)
    current_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_expenses(self, expense_amount):
        self.current_expenses += expense_amount
        self.save()

        if self.current_expenses > self.monthly_limit:
            self.send_notification_if_exceeded_limit()

    def send_notification_if_exceeded_limit(self):
        messages.warning(self.user, f"You have exceeded your $300 monthly limit.")


    def calculate_remaining_balance(self):
        remaining_balance = self.monthly_limit - self.current_expenses
        return remaining_balance







    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    