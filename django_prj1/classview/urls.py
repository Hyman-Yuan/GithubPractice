from django.conf.urls import url
from .views import DemoView

urlpatterns=[
    url(r'^demoview/$',DemoView.as_view()),
]