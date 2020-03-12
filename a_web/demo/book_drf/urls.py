from django.conf.urls import url

from book_drf import apiview_view, genericapiview_view, mixin_view, childmixin_view, viewset_view, genericviewset_view, modelviewset_view, modelviewset_view2
from rest_framework.routers import DefaultRouter
from  . import  views
urlpatterns = [
    # url(r'^books_drf/$', views.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', views.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', views.BookDRFView.as_view()),

    url(r'^books_drf/$', apiview_view.Books.as_view()),
    url(r'^book_drf/(?P<pk>\d+)$', apiview_view.Book.as_view()),
    url(r'^books_drf/(?P<pk>\d+)$', apiview_view.BookDRFView.as_view()),

    # url(r'^books_drf$', genericapiview_view.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', genericapiview_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', genericapiview_view.BookDRFView.as_view()),

    # url(r'^books_drf/$', mixin_view.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', mixin_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', mixin_view.BookDRFView.as_view()),

    # url(r'^books_drf$', childmixin_view.Books.as_view()),
    # url(r'^book_drf/(?P<pk>\d+)$', childmixin_view.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)$', childmixin_view.BookDRFView.as_view()),

    # # ViewSet路由使用
    # url(r'^books_drf$', viewset_view.Books.as_view({'get':'list','post':'create',})),
    # url(r'^books_drf/(?P<pk>\d+)$', viewset_view.BookDRFView.as_view({'put':'update','delete':'destroy','get':'retrieve'})),
    # url(r'^books_drf/(?P<pk>\d+)/lastdata$', viewset_view.BookDRFView.as_view({'get':'lastdata'})),

    # # GenericViewSet路由使用
    # url(r'^books_drf$', genericviewset_view.Books.as_view({'get': 'list', 'post': 'create', })),
    # url(r'^books_drf/(?P<pk>\d+)$',genericviewset_view.BookDRFView.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    # url(r'^books_drf/(?P<pk>\d+)/lastdata$', genericviewset_view.BookDRFView.as_view({'get': 'lastdata'})),

    # ModelViewSet路由使用
    # url(r'^books_drf/$', modelviewset_view.Books.as_view({'get': 'list', 'post': 'create', })),
    # url(r'^books_drf/(?P<pk>\d+)/$',modelviewset_view.Books.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    # # url(r'^books_drf/(?P<pk>\d+)/lastdata$', modelviewset_view.Books.as_view({'get': 'lastdata'})),
]

# # 自动生成路由,要和视图集配合使用
# router = DefaultRouter()
# router.register('books_drf', modelviewset_view.Books,basename='books')
# print(router.urls)# 打印路由
# urlpatterns += router.urls

# # 自定义生成路由,要和视图集配合使用
# router = DefaultRouter()
# router.register('books_drf', modelviewset_view2.Books,basename='books')
# print(router.urls)# 打印路由
# urlpatterns += router.urls