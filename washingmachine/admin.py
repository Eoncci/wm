from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tel', 'status', 'start', 'end')
    list_filter = ('tel', 'status', 'start', 'end')
    search_fields = ('status', 'tel')


@admin.register(Userinfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('tel', 'name', 'address')


class MyAdminSite(admin.AdminSite):
    site_header = '好医生运维资源管理系统'  # 此处设置页面显示标题
    site_title = '好医生运维'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')
# admin.site.register(Order)
# admin.site.register(Userinfo)
# admin.site.register(Wm)
# Register your models here.
