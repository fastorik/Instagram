from django.contrib import admin
from . import models
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =  ['label']
    search_fields = ['tag']

@admin.register(models.TaggedItem)
class TagAdmin(admin.ModelAdmin):
    list_display =  ['tag', 'content_object','object_id']
    ordering = ['tag', 'object_id']
    