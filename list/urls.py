from . import views
from django.urls import path


urlpatterns = [
    path('', views.ItemsList.as_view(), name='home'),
    path('hello/', views.say_hello, name='hello'),
    path('test/', views.ItemsList.as_view(), name='test'),
    path('testwo/', views.testwo, name='testwo'),
    path('additem/', views.addItem, name='addItem'),
    path('items/', views.showItems, name='items'),
    path('home/', views.home, name='home'),
    path('lists/', views.show_lists, name='lists'),
    path('create_list/', views.add_list, name='create_list'),
]