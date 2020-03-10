from django.conf.urls import url
from django.contrib import admin
from . import views, apiview_view, genericapivew_view, mixin_view, childmixin_view, viewset_view, genericviewset_view, \
    modelviewset_view
from rest_framework.routers import SimpleRouter,DefaultRouter

urlpatterns = [
    # url(r'^books_drf/$', childmixin_view.Books.as_view()),
    # url(r'^book_drf/$', childmixin_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)/$', childmixin_view.BookDRFView.as_view()),
    # ViewSet路由使用
    # url(r'^books_drf/$', viewset_view.Books.as_view({'get':'list','post':'create'})),
    # url(r'^books_drf/(?P<pk>\d+)/$', viewset_view.BookDRFView.as_view({'put':'update'})),
    # url(r'^books_drf/(?P<pk>\d+)/lastdata/$', viewset_view.BookDRFView.as_view({'get':'lastdata'})),
    # GenericViewSet路由使用
    # url(r'^books_drf/$', genericviewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books_drf/(?P<pk>\d+)/$', genericviewset_view.BookDRFView.as_view({'put': 'update'})),
    # url(r'^books_drf/(?P<pk>\d+)/lastdata/$', viewset_view.BookDRFView.as_view({'get': 'lastdata'})),

    # url(r'^books_drf/$', modelviewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books_drf/(?P<pk>\d+)/$', modelviewset_view.Books.as_view({'put': 'update','get':'retrieve','delete':'destroy'})),

]

router = DefaultRouter()
router.register('books_drf', modelviewset_view.Books, base_name='books')
print(router.urls)
urlpatterns += router.urls
