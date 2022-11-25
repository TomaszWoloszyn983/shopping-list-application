from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('lists/', views.show_lists, name='lists'),

    path('add_list/', views.add_list, name='add_list'),
    path('edit_list/<slug:slug>/', views.edit_list, name='edit_list'),
    path('delete_list/<slug:slug>/', views.delete_list, name='delete_list'),
    path(
        'show_list_items/<slug:slug>/',
        views.show_list_items, name='show_list_items'),
    path('clear_list/<slug:slug>/', views.clear_list, name='clear_list'),

    path('add_item/<slug:slug>/', views.add_item, name='add_item'),
    path(
        'edit_list_item/<int:id>/<slug:slug>/',
        views.edit_list_item, name='edit_list_item'),
    path(
        'delete_list_item/<slug:slug>/',
        views.delete_list_item, name='delete_list_item'),
    path(
        'mark_as_bought/<slug:slug>/',
        views.mark_as_bought, name='mark_as_bought'),
]
