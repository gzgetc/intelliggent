from django.conf.urls import include, url
from mainapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^index/',views.index,name='index'),
    url(r'^describ/(\S*)/$',views.describ,name='describ'),
    url(r'^about/',views.about,name='about'),
    url(r'^works/',views.works,name='works'),
]