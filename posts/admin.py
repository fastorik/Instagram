from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    fields = ['postContent','author', 'image', 'video',]
    list_display =['id', 'postContent','author', 'image']

    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related('author').\
            prefetch_related('allComments__author')


admin.site.register(Post, PostAdmin)






