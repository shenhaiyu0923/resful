
from . import views
# from django.conf.urls import url
from django.urls import path

urlpatterns = [

    path(r'', views.DetailView.as_view()),
]
