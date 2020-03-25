from django.conf.urls import url
from .views import all_coffee, coffee_detail

urlpatterns = [
    url(r'^all_coffee$', all_coffee, name='all_coffee'),
    url(r'^(?P<pk>\d+)/$', coffee_detail, name='coffee_detail')
]