from django.urls import path
from .views import view_order

urlpatterns = [
    path('', view_order, name='view_order'),
]
