from django.conf.urls import url

from book_drf import apiview_view, genericapiview_view, mixin_view
from  . import  views
urlpatterns = [
    # url(r'^books_drf$', views.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', views.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', views.BookDRFView.as_view()),

    # url(r'^books_drf$', apiview_view.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', apiview_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', apiview_view.BookDRFView.as_view()),

    # url(r'^books_drf$', genericapiview_view.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', genericapiview_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', genericapiview_view.BookDRFView.as_view()),

    url(r'^books_drf$', mixin_view.Books.as_view()),
    url(r'^book_drf/(?P<pk>\d+)$', mixin_view.Book.as_view()),
    url(r'^books_drf/(?P<pk>\d+)$', mixin_view.BookDRFView.as_view()),
]
