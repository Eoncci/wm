from django.shortcuts import render, HttpResponse
from .models import *
from .forms import OrderForm
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
            u1 = Userinfo(tel=order_form.cleaned_data['tel'],
                          name=order_form.cleaned_data['name'],
                          address=order_form.cleaned_data['address'])
            _order = Order(id=uuid.uuid1(),
                           tel=order_form.cleaned_data['tel'],
                           start=datetime.datetime.now(),
                           end=datetime.datetime.now()+datetime.timedelta(days=365*int(order_form.cleaned_data['product'])),
                           wmid=1)
            u1.save()
            _order.save()
            return HttpResponse('success!')
        return HttpResponse(json.dumps(order_form.errors))
    else:
        return HttpResponse('error!')
