from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




# 127.0.0.1:8000/cookies_demo
def cookies_demo(requset):
    response_data = HttpResponse('cookies_demo')
    # response_data.set_cookie(key='name',value='zsf')
    print(requset.COOKIES)
    return response_data


# 127.0.0.1:8000/session_demo
def session_demo(requset):
    # requset.session['age'] = 11
    # requset.session['num'] = 12
    print(requset.session.get('age'))
    data = requset.session
    return HttpResponse('session_demo')
