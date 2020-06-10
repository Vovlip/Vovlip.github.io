from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^index/$', views.index, name='index'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^onas/$', views.onas, name='onas'),
    url(r'^dostavka_oplata/$', views.dostavka_oplata, name='dostavka_oplata'),
]
