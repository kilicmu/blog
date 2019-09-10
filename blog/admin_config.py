#coding=utf-8
from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Comments, Tags, User, Filter, Headpic

class TagInline(admin.TabularInline):
    model = Tags
    list_display = ['Filter_Tags_id']
    extra=1

class CcommentInline(admin.TabularInline):
    model = Comments
    list_display = ['Ccontent']
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('a_title','a_uploadTime', 'a_readnum', 'a_likenum', 'a_isdelete', 'image_data')
    list_filter = ['a_isdelete']
    readonly_fields = ('image_data',) 
    list_per_page = 20
    search_fields = ['a_title']
    inlines=[
        TagInline,
        CcommentInline
    ]


class HeadpicAdmin(admin.ModelAdmin):
    list_display = ('h_title', 'h_content', 'image_data')
    list_per_page = 20
    search_fields = ['h_title']

class FilterAdmin(admin.ModelAdmin):
    list_display = ('Fname', )
 

class UserAdmin(admin.ModelAdmin):
    list_display = ('Uname', )