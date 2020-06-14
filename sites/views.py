from django.shortcuts import render,redirect
from django.template import loader
from .models import details
from django.http import HttpResponse

# Create your views here.
def home(request):
    page = loader.get_template("index.html")
    context = {"display":'False'}
    return HttpResponse(page.render(context, request))

def submit(request):
    if request.method == "POST":
        his_name = request.POST["his_name"]
        her_name = request.POST["her_name"]
        form = details(his_name = his_name,her_name = her_name)
        form.save()
        index=flames(his_name,her_name)
        Flames = ['You are friends', 'You are in love', "Its just affection", 'You will be endup in marriage', 'Enemies for ever','brother and sister']
        page = loader.get_template("index.html")
        context={"display":'True',"msg" : Flames[index] }
        return HttpResponse(page.render(context, request))
    else:
        page = loader.get_template("index.html")
        context = {"display":'False'}
        return HttpResponse(page.render(context, request))

def sept(c):
    list3=[]
    for i in range(0,len(c)):
        list3.append(c[i])
    return list3
def flames(a,b):
    i,j=0,0
    if len(b)>len(a):
        a,b=b,a
    list1=[]
    list2=[]
    list1=sept(a)
    list2=sept(b)
    while(i<len(list1)):
        j=0
        while(j<len(list2)):
            try:
                if list1[i]==list2[j]:
                    list1.pop(i)
                    list2.pop(j)
                else:
                    j+=1
            except:
                pass
        i+=1
    length=len(list1)+len(list2)
    return(length%6)