from django.urls import path
from .views import get_items,create_item,delete_item,update_item

urlpatterns = [
    path('get-items', get_items),
    path('create-item', create_item),
    path('update-item/<int:pk>', update_item),
    path('delete-item/<int:pk>', delete_item),
]
