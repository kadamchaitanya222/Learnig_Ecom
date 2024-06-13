from django.shortcuts import HttpResponse
from django.shortcuts import render
from student.models import sign_up


title="kadamm"




def index(request):
    users=sign_up.objects.all()
    return render(request,"index.html",{"users":users,"title":title})


