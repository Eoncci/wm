from django.shortcuts import render, HttpResponse
from .models import *
from .forms import OrderForm, QueryForm
import json
import uuid
import datetime

# Create your views here.


def index(request):
    return render(request, 'washingmachine/index.html')


def order(request):
    return render(request, 'washingmachine/order.html')


def status(request):
    return render(request, 'washingmachine/status.html')


def wm_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            try:
                Order.objects.get(tel=order_form.cleaned_data['tel'])
                return HttpResponse(handle_result(data={}, _status=0, message='you already have an order!'))
            except models.ObjectDoesNotExist:
                pass

            u1 = Userinfo(tel=order_form.cleaned_data['tel'],
                          name=order_form.cleaned_data['name'],
                          address=order_form.cleaned_data['address'])
            _order = Order(id=uuid.uuid1(),
                           tel=order_form.cleaned_data['tel'],
                           start=datetime.datetime.now(),
                           end=datetime.datetime.now() + datetime.timedelta(
                               days=365*int(order_form.cleaned_data['product'])),
                           wmid=1)
            u1.save()
            _order.save()
            return HttpResponse(handle_result(data={}, _status=1, message=''))
        return HttpResponse(json.dumps(order_form.errors))
    else:
        return HttpResponse(handle_result(data={}, _status=0, message='wrong request!'))


def query(request):
    if request.method == 'POST':
        query_form = QueryForm(request.POST)
        if query_form.is_valid():
            try:
                _temp = Order.objects.get(tel=query_form.cleaned_data['tel'])
                return HttpResponse(handle_result(data=_temp.to_dict(), _status=1, message=''))
            except models.ObjectDoesNotExist:
                return HttpResponse(handle_result(data={}, _status=0, message='tel not exit!'))
        else:
            return HttpResponse(json.dumps(query_form.errors))
    else:
        return HttpResponse(handle_result(data={}, _status=0, message='wrong request!'))


def handle_error(error: str):
    return json.dumps({'error': error})


def handle_result(data: dict, _status: int, message: str):
    return json.dumps({'data': data,
                       'status': _status,
                       'message': {'zh': message,
                                   'en': message}
                       })
