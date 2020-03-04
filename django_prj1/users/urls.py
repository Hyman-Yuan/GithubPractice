from django.conf.urls import url
from . import views


urlpatterns = [
    # 顺序传参
        # url(r'whether/([a-z]+)/(\d{4})/$',views.whether),
    # 关键字传参


    url(r'^whether/(?P<city>[a-z]+)/(?P<date>\d{4})/$',views.whether),

    url(r'^html/(?P<name>[a-z]+)/(?P<age>\d{,2})/$',views.html),

    url(r'get_method/$',views.get_method),

    url(r'post_method/$',views.post_method),

    url(r'form_data_method/$',views.form_data_method),

    url(r'json_data_method/$',views.json_data_method),

    # url(r'^index/$',views.index)
]