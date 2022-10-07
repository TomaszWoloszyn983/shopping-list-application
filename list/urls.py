from . import views
from django.urls import path


urlpatterns = [
    path('', views.ItemsList.as_view(), name='home')
]