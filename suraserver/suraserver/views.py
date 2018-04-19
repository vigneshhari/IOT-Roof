from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from nodes.models import node1 , node2 , lock
import datetime 

def node_1(request):
    data = node1.objects.all()
    if(data.count() >= 10 ):
        node1.objects.all().order_by('time')[0].delete()
    node1(time = datetime.datetime.now() , key = list(request.GET.keys())[0] , val = request.GET[list(request.GET.keys())[0]] ).save()
    print("value" , request.GET.get("val"))
    if(lock.objects.all().filter(lock = "node2").count() > 0 ):
        if(node2.objects.all().order_by('-time')[0].val == "1"):
            return HttpResponse(status = 201) 
        return HttpResponse(status = 200)   
    if( request.GET[list(request.GET.keys())[0]] == "1"):
        return HttpResponse(status = 201)
    return HttpResponse(status = 200)

def node_2(request):
    data = node2.objects.all()
    if(data.count() >= 10 ):
        node2.objects.all().order_by('time')[0].delete()
    node2(time = datetime.datetime.now() , key = list(request.GET.keys())[0] , val = request.GET[list(request.GET.keys())[0]] ).save()
    if(lock.objects.all().filter(lock = "node1").count() > 0 ):
        if(node1.objects.all().order_by('-time')[0].val == "1"):
            return HttpResponse(status = 201)
        return HttpResponse(status = 200)
    if( request.GET[list(request.GET.keys())[0]] == "1"):
        return HttpResponse(status = 201)
    return HttpResponse(status = 200)

def out(request):
    data1 = []
    data2 = []
    for i in node1.objects.all():
        data1.append({"key" : i.key , "val" : i.val , "time" : i.time}  )
    for i in node2.objects.all():
        data2.append({"key" : i.key , "val" : i.val , "time" : i.time}  )
    return render(request , "out.html" , { "data1" : data1 , "data2" : data2 })

def onnode1(request):
    node2.objects.all().delete()
    lock(lock = "node1").save()
    return HttpResponseRedirect("/out")

def onnode2(request):    
    node1.objects.all().delete()
    lock(lock = "node2").save()
    return HttpResponseRedirect("/out")

def normal(request):
    lock.objects.all().delete()
    return HttpResponseRedirect("/out")
    