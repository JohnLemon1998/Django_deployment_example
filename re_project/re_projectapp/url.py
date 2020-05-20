from django.conf.urls import url
from re_projectapp import views

app_name = 're_projectapp'

urlpatterns = [
    url(r'^registeration/$',views.register,name='register'),
]
