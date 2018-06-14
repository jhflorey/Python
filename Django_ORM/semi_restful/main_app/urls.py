from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<user_id>[0-9]+)/show$', views.show, name='show'),
    url(r'^(?P<user_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<user_id>[0-9]+)/delete$', views.delete, name='delete'),
    url(r'^(?P<user_id>[0-9]+)/update$', views.update, name='update'),
]
