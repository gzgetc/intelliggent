from django.db import models


# Create your models here.


#Photolbum tables start
class PhotoLbum(models.Model):
    imgnumber=models.IntegerField(primary_key=True)
    imgname=models.CharField(max_length=20,unique=True)
    imgtitle=models.CharField(max_length=50)
    images=models.ImageField(upload_to='photolbum')
    def __unicode__(self):
        return u'%s' %self.imgname

    class Meta:
        db_table='photolbum'

class PhotoDescrib(models.Model):
    imgnumber=models.IntegerField(primary_key=True)
    imgname=models.CharField(max_length=20,unique=True)
    imgtitle=models.CharField(max_length=50)
    images=models.ImageField(upload_to='photodescrib')
    content=models.TextField()
    def __unicode__(self):
        return u'%s' %self.imgname
    class Meta:
        db_table='photodescrib'
#AboutGather tables start
class AboutContent(models.Model):
    labelname=models.CharField(max_length=20,unique=True)
    title=models.CharField(max_length=50)
    headimg=models.ImageField(upload_to='aboutcontent')
    bottonadvert=models.ImageField(upload_to='aboutcontent')

    def __unicode__(self):
        return u'%s' %self.labelname
    class Meta:
        db_table='aboutcontent'

class AboutGather(models.Model):
    number=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,unique=True)
    images=models.ImageField(upload_to='aboutgather')
    content=models.TextField(null=True)
    def __unicode__(self):
        return u'%s' %self.name
    class Meta:
        db_table='aboutgather'





