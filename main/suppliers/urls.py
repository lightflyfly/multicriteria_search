from django.urls import path

from suppliers.views import index

urlpatterns = [
    path('', index)
]

