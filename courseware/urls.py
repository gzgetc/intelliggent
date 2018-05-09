from django.conf.urls import include, url
from courseware import views

urlpatterns = [
    url(r'^java/(\d*)/$',views.java,name='java'),
    url(r'^python/(\d*)/$',views.python,name='python'),
    url(r'^linux/(\d*)/$',views.linux,name='linux'),
    url(r'^html5/(\d*)/$',views.html5,name='html5'),
    url(r'^dbase/(\d*)/$',views.dbase,name='dbase'),
]