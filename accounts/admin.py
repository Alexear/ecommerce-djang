from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_link=('email','first_name','last_name')
    readonly =('last_login','date_joined')
    ordenring =('-date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()


# Register your models here.
admin.site.register(Account, AccountAdmin)
