from . import views
from django.urls import path


urlpatterns = [
    path('', views.ItemsList.as_view(), name='home'),
    # path('additem/', views.addItem, name='addItem'),
    path('items/', views.showItems, name='items'),
    path('home/', views.home, name='home'),
    path('lists/', views.show_lists, name='lists'),
    path('add_list/', views.add_list, name='create_list'),
    path('edit_list/<slug:slug>/', views.edit_list, name='edit_list'),
    path('delete_list/<slug:slug>/', views.delete_list, name='delete_list'),
    path('add_item/', views.add_item, name='add_item'),
]