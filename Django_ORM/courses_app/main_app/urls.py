from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/destroy/(?P<course_id>[0-9]+)$', views.destroy, name='destroy'),
    url(r'^courses/confirm_destroy/(?P<course_id>[0-9]+)$', views.confirm_destroy, name='confirm_destroy'),
    url(r'^create$', views.create, name='create'),
]