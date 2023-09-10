from django.contrib import admin

# Register your models here.
from .models import NewUser
from core.models import PhonePrefix
admin.site.register(NewUser)
admin.site.register(PhonePrefix)