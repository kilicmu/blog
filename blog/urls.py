from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name ='index'),
    url(r'detail/$', views.detail, name = 'details'),
    # url(r'p(?P<PIndex>[0-9]*)/$', views.index, name='page'),
    url(r'filte/([0-9]*)/$', views.filte, name = 'details'),
    url(r'^filte_by_time/$', views.filte_by_time, name = 'filte_by_time'),
    url(r'upload_comment/$', views.comment, name ='comment'),
    # url(r'filte/(?P<id>[0-9]*)/p(?P<PIndex>[0-9]*)/$', views.filte, name = 'details'),
]