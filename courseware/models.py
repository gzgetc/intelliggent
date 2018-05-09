from django.db import models

# Create your models here.

#course page tables start
class CourseContent(models.Model):
    labelname=models.CharField(max_length=20,unique=True)
    title=models.CharField(max_length=50)
    headimg=models.ImageField(upload_to='coursecontent')
    bottonadvert=models.ImageField(upload_to='coursecontent')

    def __unicode__(self):
        return u'%s' %self.labelname
    class Meta:
        db_table='coursecontent'



#course tables start

class Substance(models.Model):
    name=models.CharField(max_length=20,null=True)
    s_content=models.TextField(null=True)
    s_coding=models.TextField(null=True)
    s_images=models.ImageField(upload_to='javascoure',null=True)
    time = models.DateTimeField()
    delete = models.BooleanField(default=False)
    def __unicode__(self):
        return u'%s' %self.s_content
    class Meta:
        db_table='substance'


class Course(models.Model):
    c_number=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return u'%s' %self.c_name
    class Meta:
        db_table='course'

class DirectoryTitle(models.Model):
    c_name=models.ForeignKey(Course)
    title=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s%s' %(self.c_name,self.title)
    class Meta:
        db_table='directorytitle'


class Directory(models.Model):
    directorytitle=models.ForeignKey(DirectoryTitle)
    d_number=models.CharField(max_length=20)
    d_name=models.CharField(max_length=20,primary_key=True)
    content=models.ForeignKey(Substance)
    def __unicode__(self):
        return u'%s%s' %(self.d_number,self.d_name)
    class Meta:
        db_table='directory'


