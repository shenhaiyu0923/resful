from django.conf.urls import url
from  . import  views
urlpatterns = [
    url(r'^books_drf$', views.Books.as_view()),
    url(r'^book_drf/(?P<pk>\d+)$', views.Book.as_view()),
    url(r'^books_drf/(?P<pk>\d+)$', views.BookDRFView.as_view()),
]
