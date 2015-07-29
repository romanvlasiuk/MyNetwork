from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user1 = models.ForeignKey(User, related_name='author')
    user2 = models.ForeignKey(User, related_name='reciever')
    title = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateTimeField()

User.get_messages = property(lambda u: list(Message.objects.filter(user2=u)))
User.sent_messages = property(lambda u: list(Message.objects.filter(user1=u)))
User.inbox = property(lambda u: len(list(Message.objects.filter(user2=u))))
User.outbox = property(lambda u: len(list(Message.objects.filter(user1=u))))