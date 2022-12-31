from asyncio import format_helpers
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.html import format_html
# Register your models here.
class AcountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','date_joined','is_active')
    list_display_links=('email','first_name','last_name','username','date_joined','is_active')
    readonly_fields=('date_joined',)
    ordering=('date_joined',)
    fieldsets=()
    list_filter=()
    filter_horizontal=()
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;" >'.format(object.profile_picture.url))

    thumbnail.short_description="Profile Picture"
    list_display=('thumbnail','user','city','state','country')

admin.site.register(Account,AcountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
