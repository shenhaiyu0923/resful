from django.urls import path

from . import views
from . import view
urlpatterns = [
    path('signin', view.signin.as_view()),
    path('signout', view.signout.as_view()),

    path('orders', view.OrderView.as_view()),
    path('customers', view.CustomerView.as_view()),
    path('medicines', view.MedicinesView.as_view()),


    # path('orders', views.OrderView.as_view()),
    # path('customers', views.CustomerView.as_view()),
    # path('medicines', views.MedicinesView.as_view()),
]