from django import forms


class OrderForm(forms.Form):
    tel = forms.CharField(required=True,
                          max_length=15,
                          error_messages={'required': 'tel 不能为空',
                                          'max_length': '输入过长'})
    name = forms.CharField(required=True,
                           error_messages={'required': 'name 不能为空'})
    address = forms.CharField(required=True,
                              error_messages={'required': 'address 不能为空'})
    product = forms.CharField(required=True,
                              error_messages={'required': 'product 不能为空'})


class QueryForm(forms.Form):
    tel = forms.CharField(required=True,
                          max_length=15,
                          error_messages={'required': 'tel 不能为空',
                                          'max_length': '输入过长'})
