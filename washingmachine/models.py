# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    tel = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=750)

    def __str__(self):
        return self.tel

    class Meta:
        db_table = 'userinfo'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45, default='', null=False)
    should_pay = models.CharField(max_length=45, default='0', null=False)
    years = models.CharField(max_length=45, default='0', null=False)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'product'


class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=45)
    tel = models.ForeignKey(UserInfo)
    start = models.CharField(max_length=45)
    end = models.CharField(max_length=45)
    wmid = models.CharField(max_length=15)
    status = models.CharField(max_length=45, default='init')
    deposit = models.CharField(max_length=45, default='0')
    product = models.ForeignKey(Product, default=0)
    paid = models.CharField(max_length=45, default='0')

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        db_table = 'order'


class Wm(models.Model):
    wmid = models.CharField(primary_key=True, max_length=15)
    status = models.CharField(max_length=45)

    class Meta:
        db_table = 'wm'


class Code(models.Model):
    tel = models.CharField(primary_key=True, max_length=15)
    code = models.CharField(max_length=15)
    result = models.CharField(max_length=150, null=True)
    time = models.DateTimeField()

    class Meta:
        db_table = 'code'
