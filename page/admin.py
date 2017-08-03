from django.contrib import admin

# Register your models here.

from page.models import Category, BlogArticle, Good

admin.site.register(Category)
admin.site.register(BlogArticle)
admin.site.register(Good)