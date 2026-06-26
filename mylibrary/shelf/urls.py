from django.urls import path
from .views import bookstore_view

urlpatterns = [
    path('bookstore_view', bookstore_view, name="bookstore_view"),
]