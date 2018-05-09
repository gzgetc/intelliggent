#coding:utf-8
from django.contrib import admin
from mainapp.models import *
# Register your models here.


#index PhotoLbumAdmin start
class PhotoLbumAdmin(admin.ModelAdmin):
    list_display = ['imgnumber','imgname','imgtitle','images']
    list_filter = ['imgnumber']
    search_fields = ['imgname']
    list_per_page = 4
    fieldsets = [
        ('图片信息', {'fields': ['imgnumber', 'imgname']}),
        ('图片标题', {'fields': ['imgtitle']}),
        ('图片', {'fields': ['images']}),
    ]

class PhotoDescribAdmin(admin.ModelAdmin):
    list_display = ['imgnumber','imgname','imgtitle','images','content']
    list_filter = ['imgnumber']
    search_fields = ['imgname']
    list_per_page = 10

    fieldsets = [
        ('图片信息', {'fields': ['imgnumber', 'imgname']}),
        ('图片标题', {'fields': ['imgtitle']}),
        ('图片', {'fields': ['images','content']}),
    ]


admin.site.register(PhotoLbum,PhotoLbumAdmin)
admin.site.register(PhotoDescrib,PhotoDescribAdmin)


#about AboutGatherAdmin start

class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['labelname', 'title', 'headimg', 'bottonadvert']
    list_filter = ['labelname']
    search_fields = ['labelname']
    list_per_page = 1

    fieldsets = [
        ('文化页面记录信息', {'fields': ['labelname']}),
        ('页面标题', {'fields': ['title']}),
        ('页面头部图片', {'fields': ['headimg']}),
        ('页面底部广告', {'fields': ['bottonadvert']}),
    ]

class AboutGatherAdmin(admin.ModelAdmin):
    list_display = ['number','name','images','content']
    list_filter = ['number']
    search_fields = ['name']
    list_per_page = 10

    fieldsets = [
        ('文化记录信息',{'fields':['number','name']}),
        ('文化记录图片',{'fields':['images']}),
        ('文化记录内容',{'fields':['content']}),
    ]


admin.site.register(AboutGather,AboutGatherAdmin)
admin.site.register(AboutContent,AboutContentAdmin)