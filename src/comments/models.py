from django.db import models
from django.conf import settings
from posts.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404, redirect


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
   # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id') 
    # instead of linking to a post only, we'll be using a generic foreign key to allow us to add a comment to any new app installed

    def __str__(self):
        return self.user.username
    class Meta:
        ordering = ['timestamp']

@receiver(post_save, sender= Comment)
def increment_comment(instance, created, **kwargs):
	if created:
		user = get_object_or_404(Comment, id=instance.id)
		#instance.post_comments += 1
		print(instance.id, "signal", user)
		instance.save()



#post_save.connect(instance, created, **kwargs)
