from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages')
    message = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_messages")
    created_datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.note

    class Meta:
        ordering = ['-id']