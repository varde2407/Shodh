from django.conf.urls import url

from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    url(r"^$", views.ListGroups.as_view(), name="all"),
    url(r"^your/$", views.ListGroups2.as_view(), name="yourall"),
    url(r"^btp/$", views.ListGroupsBTP.as_view(), name="btp"),
    url(r"^new/$", views.CreateGroup.as_view(), name="create"),
    url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    path('searchbar', views.searchbar, name='searchbar'),
    #url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    #url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
