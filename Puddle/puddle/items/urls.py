from django.urls import path
from items import views


app_name = "items"

urlpatterns = [
    path("<int:pk>", views.detail, name="detail"),
    path("create/", views.create_item, name="create"),
    path("edit/<int:item_id>", views.edit_item, name="edit"),
]