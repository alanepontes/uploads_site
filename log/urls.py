from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^post_document_detail/(?P<id>[0-9]+)/$', views.post_document_detail, name='post_document_detail'),
    url(r'^post_document_new/new/$', views.post_document_new, name='post_document_new'),
    url(r'^post_document_download/(?P<id>[0-9]+)$', views.post_document_download, name='post_document_download'),
    url(r'^post_document_edit/(?P<id>[0-9]+)/edit/$', views.post_document_edit, name='post_document_edit'),
    url(r'^post_document_delete/(?P<id>[0-9]+)$', views.post_document_delete, name='post_document_delete'),
]
