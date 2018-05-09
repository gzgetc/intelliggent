from django.shortcuts import render
from courseware.models import *
from django.core.paginator import *


# Create your views here.

def java(request,pindex):
    list = Directory.objects.filter(directorytitle__c_name__c_name='Java').order_by('d_number')
    paginator = Paginator(list,20)
    javacourse=paginator.page(int(pindex))

    javacontent=CourseContent.objects.filter(labelname='Java')

    context = {'javacourse': javacourse,
                'javacontent':javacontent,
               }

    return render(request,'courseware/java.html',context)

def python(request,pindex):
    list = Directory.objects.filter(directorytitle__c_name__c_name='Python').order_by('d_number')
    paginator = Paginator(list,20)
    pythoncourse=paginator.page(int(pindex))

    pythoncontent=CourseContent.objects.filter(labelname='Python')

    context = {'pythoncourse': pythoncourse,
                'pythoncontent':pythoncontent,
               }

    return render(request,'courseware/python.html',context)

def linux(request,pindex):
    list = Directory.objects.filter(directorytitle__c_name__c_name='Linux').order_by('d_number')
    paginator = Paginator(list,20)
    linuxcourse=paginator.page(int(pindex))

    linuxcontent=CourseContent.objects.filter(labelname='Linux')

    context = {'linuxcourse': linuxcourse,
                'linuxcontent':linuxcontent,
               }

    return render(request,'courseware/linux.html',context)

def html5(request,pindex):
    list = Directory.objects.filter(directorytitle__c_name__c_name='HTML5').order_by('d_number')
    paginator = Paginator(list,20)
    html5course=paginator.page(int(pindex))

    html5content=CourseContent.objects.filter(labelname='HTML5')

    context = {'html5course': html5course,
                'html5content':html5content,
               }

    return render(request,'courseware/html5.html',context)

def dbase(request,pindex):
    list = Directory.objects.filter(directorytitle__c_name__c_name='DBase').order_by('d_number')
    paginator = Paginator(list,20)
    dbasecourse=paginator.page(int(pindex))

    dbasecontent=CourseContent.objects.filter(labelname='DBase')

    context = {'dbasecourse': dbasecourse,
                'dbasecontent':dbasecontent,
               }

    return render(request,'courseware/dbase.html',context)






