from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.showItems, name='items'),
    path('lists/', views.show_lists, name='lists'),
    path('add_list/', views.add_list, name='create_list'),
    path('edit_list/<slug:slug>/', views.edit_list, name='edit_list'),
    path('delete_list/<slug:slug>/', views.delete_list, name='delete_list'),
    path('show_list_items/<slug:slug>/', views.show_list_items, name='show_list_items'),
    path('clear_list/<slug:slug>/', views.clear_list, name='clear_list'),
    # path('show_list_items/<slug:slug>/add_item/', views.add_item, name='add_item'),
    # path('add_item/', views.add_item, name='add_item'),
    path('add_item/<slug:slug>/', views.create_item, name='add_item'),
    path('delete_item/<slug:slug>/', views.delete_item, name='delete_item'),
    path('edit_item/<slug:slug>/', views.edit_item, name='edit_item'),
    path('mark_as_bought/<slug:slug>/', views.mark_as_bought, name='mark_as_bought'),

# urls for logged in users views:
    path('create_extended_item/', views.create_extended_item, name='create_extended_item'),
]