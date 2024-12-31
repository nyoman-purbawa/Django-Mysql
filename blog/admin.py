from django.contrib import admin

from .models import Article,Publication, Render, Tag, ReadList

# Register your models here.

admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Render)
admin.site.register(Tag)
admin.site.register(ReadList)