from django.conf.urls import url
from core import views

urlpatterns =[
    url(r'^servicios/$', views.servicios_lista),
    url(r'^servicios/(?P<pk>[0-9]+)/$', views.servicio_detail),
]
