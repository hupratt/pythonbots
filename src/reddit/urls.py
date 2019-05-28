from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^random-reddit-article/$', views.get_reddit_article),
    url(r'^classify/', views.get_classification),
    ]