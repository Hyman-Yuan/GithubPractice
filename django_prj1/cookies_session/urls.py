from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cookies_demo/$',views.cookies_demo),
    url(r'^session_demo/$',views.session_demo),
]