from django.conf.urls import include, url
from django.contrib import admin
import social.apps.django_app.urls
import socshop.views


urlpatterns = [
    url(r'^$', socshop.views.home, name='home'),
    url(r'^accounts/logout/$', socshop.views.account_logout, name='logout'),
    url(r'^accounts/login/$', socshop.views.home, name='login'),
    url(r'^accounts/profile/$', socshop.views.account_profile, name='profile'),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]
