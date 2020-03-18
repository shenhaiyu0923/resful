from django.conf.urls import url
from  . import  views
urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookView.as_view()),
    url(r'^book/$', views.BookView.as_view()),
]


#http://127.0.0.1:8000/books/1   有效
#http://127.0.0.1:8000/books?id=1   无效