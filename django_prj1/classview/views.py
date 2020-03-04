from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# GET/POST 127.0.0.1:8000/demoview/

class DemoView(View):

    def get(self,request):

        return HttpResponse('接收到GET請求')

    def post(self,request):

        return HttpResponse('接收到POST請求')


# Create your views here.
