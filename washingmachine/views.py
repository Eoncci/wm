from django.shortcuts import render, HttpResponse
import requests
from .models import *
from .forms import OrderForm, QueryForm
import json
import uuid
import random
import datetime
from yisanji.settings import MESSAGE_URL
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


def index(request):
    return render(request, 'washingmachine/index.html')


def order(request):
    return render(request, 'washingmachine/order.html')


def status(request):
    return render(request, 'washingmachine/status.html')


@require_http_methods(["POST"])
def wm_order(request):
    order_form = OrderForm(request.POST)

    # if request.POST.get('code') and order_form.is_valid():
    if order_form.is_valid():
        # code = request.POST.get('code')
        # try:
        #     _code = Code.objects.get(tel=order_form.cleaned_data['tel'])
        #     if code == _code.code:
        #         pass
        #     else:
        #         return HttpResponse(handle_result(data={}, _status=0, message='you input the wrong code'))
        # except models.ObjectDoesNotExist:
        #     return HttpResponse(handle_result(data={}, _status=0, message='you did not have code'))

        try:
            Order.objects.get(tel=order_form.cleaned_data['tel'])
            return HttpResponse(handle_result(data={}, _status=0, message='you already have an order!'))
        except models.ObjectDoesNotExist:
            pass

        u1 = UserInfo(tel=order_form.cleaned_data['tel'],
                      name=order_form.cleaned_data['name'],
                      address=order_form.cleaned_data['address'])
        _product = Product.objects.get(id=int(order_form.cleaned_data['product']))
        _order = Order(id=uuid.uuid1(),
                       tel=u1,
                       start=datetime.datetime.now(),
                       end=datetime.datetime.now() + datetime.timedelta(
                           days=365*int(order_form.cleaned_data['product'])),
                       product=_product,
                       wmid=1)
        u1.save()
        _order.save()
        return HttpResponse(handle_result(data={}, _status=1, message=''))
    return HttpResponse(json.dumps(order_form.errors))


@require_http_methods(["GET"])
@ensure_csrf_cookie
def generate_code(request):
    tel = request.GET.get('tel')
    if not tel:
        return HttpResponse(handle_result(data={}, _status=0, message='need tel'))
    try:
        code = Code.objects.get(tel=tel)
        if datetime.datetime.now().timestamp() >= \
                (code.time + datetime.timedelta(minutes=3)).timestamp():
            code.code = random_code(4)
            code.time = datetime.datetime.now()
            code.result = send_message(tel=tel, code=code.code)
            if check_message(code.result):
                code.save(update_fields=['code', 'result', 'time'])
                return HttpResponse(handle_result(data={}, _status=1, message='generate success'))
            else:
                return HttpResponse(handle_result(data={}, _status=0, message='generate failed'))
        return HttpResponse(handle_result(data={}, _status=0, message='wait 3 min'))
    except models.ObjectDoesNotExist:
        code = random_code(4)
        # 这里可能需要校验一下电话格式
        result = send_message(tel=tel, code=code)
        if check_message(result):
            _c = Code(tel=tel, code=code, result=result, time=datetime.datetime.now())
            _c.save()
            return HttpResponse(handle_result(data={}, _status=1, message='generate success'))
        else:
            return HttpResponse(handle_result(data={}, _status=0, message='generate failed'))


def check_message(message: str):
    # {"returnstatus": "Success", "message": "操作成功", "remainpoint": "18", "taskID": "1708083333024273",
    #  "successCounts": "1"}
    message = json.loads(message)
    if message.get('returnstatus') == 'Success':
        return message.get('taskID')
    return ''


@require_http_methods(["POST"])
def query(request):
    query_form = QueryForm(request.POST)
    if query_form.is_valid():
        try:
            _temp = Order.objects.get(tel=query_form.cleaned_data['tel'])
            final = _temp.to_dict()
            final['tel'] = final['tel'].tel
            final['product'] = final['product'].id
            return HttpResponse(handle_result(data=final, _status=1, message=''))
        except models.ObjectDoesNotExist:
            return HttpResponse(handle_result(data={}, _status=0, message='tel not exit!'))
    else:
        return HttpResponse(json.dumps(query_form.errors))


def handle_error(error: str):
    return json.dumps({'error': error})


def handle_result(data: dict, _status: int, message: str):
    return json.dumps({'data': data,
                       'status': _status,
                       'message': {'zh': message,
                                   'en': message}
                       })


def send_message(tel: str, code: str):
    message = '您的验证码为' + code + '，有效期3分钟，请速去填写。【宜叁集】'  # 中文需要先转码
    url = MESSAGE_URL.format(tel, message)
    req = requests.get(url).text
    return req


def random_code(length: int=4):
    list_sample = [str(num) for num in range(0, 10)] + [chr(num) for num in range(97, 112)]
    code = "".join(random.sample(list_sample, length))
    return str(code)
