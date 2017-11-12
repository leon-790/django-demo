from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index/$', views.index),
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^article/edit/(?P<article_id>[0-9]+)$', views.edit_article, name='edit_article'),
    url(r'^article/update/$', views.save_edit_article, name='update_article'),
    url(r'^article/new$', views.new_article, name="new_article"),
    url(r'^article/save/$', views.save_new_article, name="create_article"),
    url(r'^article/delete/(?P<article_id>[0-9]+)$', views.delete_article, name='delete_article')
]
