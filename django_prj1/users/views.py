from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def whether(request,date,city):
    print(f'城市： {city}')
    print(f'日期： {date}')
    body = f'城市：{city}日期：{date}'
    return HttpResponse(body)


def html(request,name,age):
    json_data = [
        {'姓名':f'{name}'},
        {'年龄':f'{age}'}
    ]

    return HttpResponse(json_data)


# 浏览器向服务器传递参数的几种方法
# 1.URL路径传参 （位置参数：顺序传参；  关键字传参  正则组中 字符串别名 该名称与 函数的形参 相同

def get_method(request):
    querr_dict = request.GET
    return HttpResponse('get_method')

# 2.查询字符串传参  ？a=1&&b=2&&a=100  此类形式的参数
#       POST请求过程中QuerryDict 对象的get方法只会获取到 表单数据
def post_method(request):
    query_dict = request.POST
    # print(query_dict.get('a'))
    print(query_dict.get('name'))
    return HttpResponse('post_method')


# 3 请求报文中的请求体：
#   3.1 form data 表单标签

def form_data_method(request):
    query_dict = request.POST
    print(query_dict.dict())
    return HttpResponse('form_data_method')

#   3.2 提交JSON格式的数据

def json_data_method(requset):
    data = requset.body
    # print(type(data))
    data1 = data.decode()
    print(type(data1))
    # 直接转为字典
    # data2 = eval(data1)
    # print(type(data2))

    json_data = json.loads(data1)

    print(type(json_data))


    return HttpResponse('json_data_method')

# # 127.0.0.1:8000/index/
# def index(request):
#     return HttpResponse('users.index')
