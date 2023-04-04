import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from items.models import Item
from message.models import MessageModel


@login_required
def send_message(request, item_id: int):
    if request.method == "POST":
        item = Item.objects.get(pk=item_id)
        receiver = item.created_by
        message = MessageModel.objects.create(
            sender=request.user,
            receiver=receiver,
            message=request.POST["message"],
            about_item=item,
        )
        message.save()

        return redirect(f"../../items/{item_id}", pk=item_id)
    else:
        return render(
            request,
            "message/send_message.html",
            {
                "request": request,
                "item_id": item_id,
            }
        )

@login_required
def inbox(request):
    messages = MessageModel.objects.filter(receiver=request.user)
    return render(
        request,
        "message/inbox.html",
        {
            "request": request,
            "messages": messages,
        }
    )