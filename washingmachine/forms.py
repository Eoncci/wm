from django import forms


class OrderForm(forms.Form):
    tel = forms.CharField(required=True,
                          error_messages={'required': 'tel 不能为空'})
    name = forms.CharField(required=True,
                           error_messages={'required': 'name 不能为空'})
    address = forms.CharField(required=True,
                              error_messages={'required': 'address 不能为空'})
    product = forms.CharField(required=True,
                              error_messages={'required': 'product 不能为空'})
