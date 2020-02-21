from django.urls import path
from . import views

urlpatterns =[
    path('list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('remove_todo/<int:todo_id>', views.remove_todo_item, name='remove_todo_item')
]
