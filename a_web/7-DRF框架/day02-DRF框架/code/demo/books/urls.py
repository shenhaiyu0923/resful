from django.conf.urls import url
from django.contrib import admin
from  . import  views
urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
]
