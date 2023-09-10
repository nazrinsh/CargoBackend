from django.db import models
from django.core.exceptions import ValidationError

class PhonePrefix(models.Model):
    prefix = models.CharField(max_length=6, default='')

    def clean(self):
        if self.prefix not in ['+99450', '+99451', '+99410', '+99455', '+99499', '+99470', '+99477']:
            raise ValidationError("It's not a valid phone prefix")
