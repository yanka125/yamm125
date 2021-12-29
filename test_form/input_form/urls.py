from django.urls import path

from .views import index, complete

urlpatterns = [
    path('', index),
    path('submitted_forms/', complete),
]
