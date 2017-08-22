from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tel', 'status', 'start', 'end', 'address')
    list_filter = ('tel', 'status', 'start', 'end')
    search_fields = ('status', 'tel')

    @staticmethod
    def address(obj):
        return obj.tel.address


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('tel', 'name', 'address')
# admin.site.register(Order)
# admin.site.register(Userinfo)
# admin.site.register(Wm)
# Register your models here.
