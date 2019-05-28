from django.conf.urls import url
from . import views
from .views import PostLikeToggle
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.list, name = 'list'),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name = 'post_update'),
    url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
    url(r'^(?P<id>\d+)/delete/$', views.delete, name = 'delete'),
    url(r'^(?P<id>\d+)/like/$', PostLikeToggle.as_view(), name = 'like-toggle'),

    url(r'^1/1/$', views.WORDEXCEL, name = 'WORDEXCEL'), 
    url(r'^2/2/$', views.kaggle, name = 'kaggle'), 
    url(r'^3/3/$', views.JIRA11, name = 'JIRA11'), 
    url(r'^4/4/$', views.linkedinparser, name = 'linkedinparser'), 
    url(r'^5/5/$', views.JIRA21, name = 'JIRA21'), 
    url(r'^6/6/$', views.JIRA31, name = 'JIRA31'), 
    url(r'^7/7/$', views.heroku, name = 'heroku'), 
    url(r'^8/8/$', views.AUTO1, name = 'AUTO1'), 
    url(r'^9/9/$', views.AUTO2, name = 'AUTO2'), 
    url(r'^10/10/$', views.AUTO3, name = 'AUTO3'), 
    url(r'^11/11/$', views.pi, name = 'pi'), 
    url(r'^12/12/$', views.imdb, name = 'IMDB'), 
    url(r'^13/13/$', views.imdb2, name = 'IMDB2'), 
    url(r'^14/14/$', views.imdb3, name = 'IMDB3'), 
    url(r'^15/15/$', views.aws, name = 'aws'), 
    url(r'^16/16/$', views.Quandl, name = 'quandl'),
    url(r'^17/17/$', views.JIRA12, name = 'JIRA12'),
    url(r'^18/18/$', views.JIRA13, name = 'JIRA13'),    
    url(r'^48/48/$', views.kaggle2, name = 'kaggle2'),
    url(r'^20/20/$', views.reddit, name = 'reddit'),
    url(r'^21/21/$', views.neural_net1, name = 'neural_net1'),

    ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)