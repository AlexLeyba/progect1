from django.contrib import admin
from django.urls import path
from firstapp.views import form_set, main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/', form_set),
    path('', main_page),
]
