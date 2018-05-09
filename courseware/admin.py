#coding:utf-8
from django.contrib import admin
from courseware.models import *
# Register your models here.


#course admin tables start
class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_number','c_name']
    list_filter = ['c_number']
    search_fields = ['c_name']
    list_per_page = 20

    fieldsets = [
        ('课程编号',{'fields':['c_number']}),
        ('课程名称',{'fields':['c_name']}),
    ]

class DirectoryTitleAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'title']
    list_filter = ['c_name','title']
    search_fields = ['title']
    list_per_page = 20

    fieldsets = [
        ('课程名称', {'fields': ['c_name']}),
        ('目录标题', {'fields': ['title']}),
    ]

class DirectoryAdmin(admin.ModelAdmin):
    list_display = ['directorytitle', 'd_number','d_name','content']
    list_filter = ['directorytitle','d_name']
    search_fields = ['d_name']
    list_per_page = 20
    fieldsets = [
        ('目录标题', {'fields': ['directorytitle']}),
        ('目录编号', {'fields': ['d_number']}),
        ('目录名称', {'fields': ['d_name']}),
        ('课程内容', {'fields': ['content']}),
    ]

class SubstanceAdmin(admin.ModelAdmin):
    list_display = ['name','s_content', 's_coding', 's_images','time','delete']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20
    fieldsets = [
        ('章节名称', {'fields': ['name']}),
        ('课程内容', {'fields': ['s_content']}),
        ('课程代码', {'fields': ['s_coding']}),
        ('课程图解', {'fields': ['s_images']}),
        ('更新时间', {'fields': ['time','delete']}),
    ]


admin.site.register(Course,CourseAdmin)
admin.site.register(DirectoryTitle,DirectoryTitleAdmin)
admin.site.register(Directory,DirectoryAdmin)
admin.site.register(Substance,SubstanceAdmin)


#course page admin start

class CourseContentAdmin(admin.ModelAdmin):
    list_display = ['labelname', 'title', 'headimg', 'bottonadvert']
    list_filter = ['labelname']
    search_fields = ['labelname']
    list_per_page = 1

    fieldsets = [
        ('页面记录信息', {'fields': ['labelname']}),
        ('页面标题', {'fields': ['title']}),
        ('页面头部图片', {'fields': ['headimg']}),
        ('页面底部广告', {'fields': ['bottonadvert']}),
    ]

admin.site.register(CourseContent,CourseContentAdmin)