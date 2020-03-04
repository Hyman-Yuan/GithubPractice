from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),

    url(r'^json_data/$',views.json_data,name='ls'),

    url(r'^redirect_data/$',views.redirect_data),

]