from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process/(?P<item_id>[0-9])$', views.process, name='process'),
    url(r'^clear$', views.clear, name='clear'),
    url(r'^checkout$', views.checkout, name='checkout'),
]
