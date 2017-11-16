from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^post/blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/about/$', views.about, name='about'),
    url(r'^post/blog_single/$', views.blog_single, name='blog_single'),
    url(r'^post/blog/$', views.blog, name='blog'),
    url(r'^post/contact/$', views.contact, name='contact'),
    url(r'^post/features/$', views.features, name='features'),
    # url(r'^post/home/$', views.post_new, name='home'),
    url(r'^post/portfolio/$', views.portfolio, name='portfolio'),
    # url(r'^post/project_sample/$', views.project_sample, name='project_sample'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/titanic/$', views.titanic, name='titanic'),
]
