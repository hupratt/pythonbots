from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^random-movie-quote/$', views.quote_json),
    url(r'^random-famous-quote/$', views.famous_quote_json),

    ]
    