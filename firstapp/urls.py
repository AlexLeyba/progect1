from django.contrib import admin
from django.urls import path, re_path
from firstapp.views import *

urlpatterns = [
    path('admin/', admin),
    path('admin1/', form_set),
    path('', main_page),
    re_path('^element/(?P<x>\w+)/$', cnt),
    re_path('^articles/(?P<x>\w+)/$', cnt),
    path('admin/articles/add/', add),
    path('admin/articles', articles),
    re_path('^admin/articles_del/(?P<content>\w+)/$', articles_del),
    re_path('^admin/articles/edit/(?P<slug>\w+)/$', articles_edit),

]
