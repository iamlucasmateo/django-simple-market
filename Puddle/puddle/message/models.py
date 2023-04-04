from django.db import models

from django.contrib.auth.models import User

from items.models import Item


class MessageModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    about_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="about_item")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"

    class Meta:
        ordering = ["-created_at"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.sender == self.receiver:
            raise ValueError("Sender and receiver can't be the same person")

