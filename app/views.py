from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def form(request):
    if request.method=='POST':
        tn=request.POST.get('top')
        t=topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse("data sumbitted successfully")
        
    return render(request, 'form.html')
def form1(request):
    a=topic.objects.all()
    d={'tops':a}
    if request.method=='POST':
        top=request.POST.get('top')
        na=request.POST.get('na')
        ur=request.POST.get('ur')
        t=topic.objects.get_or_create(topic_name=top)[0]
        t.save()
        s=webpage.objects.get_or_create(topic_name=t,name=na,url=ur)[0]
        s.save()
        return HttpResponse("create successfully")
    return render(request, 'form1.html',d)
