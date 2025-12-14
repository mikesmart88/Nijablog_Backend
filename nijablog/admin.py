from django.contrib import admin
from .models import Article, Nationality, Tag, ArticleFile

# Register your models here.

admin.site.site_header = 'Web Frame(FM) Admin'
admin.site.index_title = 'Blog API'
admin.site.site_title = 'Web Adminstrator'

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(ArticleFile)
admin.site.register(Nationality)
