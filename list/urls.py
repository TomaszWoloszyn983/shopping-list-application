from . import views
from django.urls import path


urlpatterns = [
    path('', views.ItemsList.as_view(), name='home'),
    path('hello/', views.say_hello, name='hello'),
    path('test/', views.test, name='test'),
    path('testwo/', views.testwo, name='testwo'),
    path('additem/', views.addItem, name='addItem')
]