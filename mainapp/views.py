from django.shortcuts import render
from mainapp.models import *

# Create your views here.

def index(request):

    # photolbum make data start
    photolbumone = PhotoLbum.objects.filter(imgnumber=1)
    photolbumtwo = PhotoLbum.objects.filter(imgnumber=2)
    photolbumthree = PhotoLbum.objects.filter(imgnumber=3)
    photolbumfour = PhotoLbum.objects.filter(imgnumber=4)

    #photodescrib make data start
    photodescrib = PhotoDescrib.objects.all()


    centext = {
        # photolbum start
        'photolbumone': photolbumone,
        'photolbumtwo': photolbumtwo,
        'photolbumthree': photolbumthree,
        'photolbumfour': photolbumfour,
        #photodescrib start
        'photodescrib': photodescrib,


    }
    return render(request,'mainapp/index.html',centext)



def describ(request,imgroute):
    describdetail=PhotoDescrib.objects.filter(imgname = imgroute)

    centext={
        'describdetail':describdetail,
    }
    return render(request,'mainapp/describ.html',centext)


def about(request):
    aboutgather=AboutGather.objects.all()
    aboutcontent=AboutContent.objects.all()

    centext={
        'aboutgather':aboutgather,
        'aboutcontent':aboutcontent,
    }
    return render(request,'mainapp/about.html',centext)


def works(request):

    centext={

    }
    return render(request,'mainapp/works.html',centext)