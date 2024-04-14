from django.contrib import admin
from .models import Author, Tag, Post, Comment, Pricing, Friends, Category, About


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']
    filter_horizontal = ['tag']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Pricing)
admin.site.register(About)
admin.site.register(Friends)
admin.site.register(Category)
