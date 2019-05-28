# users/urls.py
# from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # url('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', views.login_signup_page, name = 'login'), 
    # url(r'^login/$', login, {'template_name':'posts/login_signup_page.html'}),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^profile/$', views.profile, name = 'profile'), 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
