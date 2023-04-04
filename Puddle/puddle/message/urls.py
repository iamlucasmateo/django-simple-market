from django.urls import path
from message import views


app_name = "message"

urlpatterns = [
    path("send_message/<int:item_id>", views.send_message, name="send_message"),
    path("inbox/", views.inbox, name="inbox"),
]