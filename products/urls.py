from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_product),
    path('detail/<int:pk>', detail_product),
    path('create/', create_product),
    path('update/<int:pk>', update_product),
    path('delete/<int:pk>', delete_product),
]