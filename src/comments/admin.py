from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['user','content_type','object_id','timestamp','content']
	class Meta:
		model = Comment



admin.site.register(Comment)