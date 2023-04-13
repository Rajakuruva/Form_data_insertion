from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *

def Insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        print(request.POST)
        return HttpResponse("Data submitted succesffully Comleted")

    return render(request,'Insert_topic.html')

def Insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        nam=request.POST['nm']
        uls=request.POST['ur']
        el=request.POST['em']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        wo=Webpage.objects.get_or_create(topic_name=to,name=nam,url=uls,email=el)[0]
        wo.save()
        print(request.POST)
        return HttpResponse("Data submit Succesffully Completed")
    return render(request,'Insert_webpage.html')

def Insert_Access(request):
    if request.method=='POST':
        tp=request.POST['tn']
        nam=request.POST['nm']
        uls=request.POST['ur']
        el=request.POST['el']
        Ath=request.POST['at']
        dta=request.POST['dt']
        to=Topic.objects.get_or_create(topic_name=tp)[0]
        to.save()
        wo=Webpage.objects.get_or_create(topic_name=to,name=nam,url=uls,email=el)[0]
        wo.save()
        ao=AccessRecord.objects.get_or_create(name=wo,author=Ath,dete=dta)[0]
        ao.save()
        return HttpResponse("Data submit Succesffully Completed")
    return render(request,'Insert_Access.html')