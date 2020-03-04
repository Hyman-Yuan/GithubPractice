from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django import http
# Create your views here.

# 127.0.0.1:8000/index/
def index(request):
    return HttpResponse('response_file.index')


# 127.0.0.1:8000/json_data/
def json_data(request):
    data = {
        'keys': "values",
        'name': 'zhangsan'
    }

    return http.JsonResponse(data)



# 127.0.0.1:8000/redirect_data/
def redirect_data(request):

    return redirect('response_file:ls')