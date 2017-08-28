from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('tel', 'status', 'start', 'end', 'deposit', 'address', 'product_info', 'should_pay', 'paid')
    list_filter = ('tel', 'status', 'start', 'end',)
    ordering = ('-start',)
    search_fields = ('status', 'tel__tel')
    list_editable = ('paid',)
    actions=['change_deposit_1', 'change_deposit_0']

    def change_deposit_1(self, request, queryset):
        queryset.update(deposit=1)
        self.message_user(request, '更改押金缴纳状态为已缴纳')

    def change_deposit_0(self, request, queryset):
        queryset.update(deposit=0)
        self.message_user(request, '更改押金缴纳状态为未缴纳')
    change_deposit_1.short_description = '更改押金缴纳状态为已缴纳'
    change_deposit_0.short_description = '更改押金缴纳状态为未缴纳'

    @staticmethod
    def address(obj):
        return obj.tel.address

    @staticmethod
    def product_info(obj):
        return obj.product.id

    @staticmethod
    def should_pay(obj):
        return obj.product.should_pay


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('tel', 'name', 'address')
    list_editable = ('address',)


@admin.register(Product)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'years', 'should_pay')
    list_editable = ('description', 'years', 'should_pay',)
# admin.site.register(Order)
# admin.site.register(Userinfo)
# admin.site.register(Wm)
# Register your models here.
