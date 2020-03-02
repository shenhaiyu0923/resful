from django.conf.urls import url
from django.contrib import admin
from  . import  views
urlpatterns = [
    url(r'^books_drf/$', views.Books.as_view()),
    url(r'^book_drf/$', views.Book.as_view()),
    #url(r'^book_drf/(?P<pk>\d+)$', views.Book.as_view()),
]