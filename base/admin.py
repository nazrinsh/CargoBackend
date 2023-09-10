from django.contrib import admin

from .models import Currency, Country
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sign', 'rate')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Country)

