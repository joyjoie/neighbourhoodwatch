from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^neighbourhood/(\d+)',views.neighbourhood,name ='neighbourhood'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^profile',views.my_profile, name='myprofile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^search/', views.search, name='search'),
    url(r'^business/',views.business,name ='business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)