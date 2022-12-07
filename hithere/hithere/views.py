from django.http import HttpResponse
from django.shortcuts import render,redirect
from hello.models import Task,CompletedTask
def addtodo(request):
        try:
            title=request.POST.get('TITLE')
            desc=request.POST.get('description')
            ins=Task(title=title,desc=desc)
            ins.save()
        except:
            pass
        return render(request,'pd.htm')

def listpage(request):
    mydata=Task.objects.all().values()
    data={'mydata':mydata}
    return render(request,'pd2.htm',data)

def completed(request,list_id):
    item=Task.objects.get(id=list_id)
    comp=CompletedTask(title=item.title,desc=item.desc)
    comp.save()
    item.delete()
    return redirect('home')

def completedlist(request):
    item=CompletedTask.objects.all().values()
    dictcomp={'item':item}
    return render(request,'pd3.htm',dictcomp)

def clearallcomp(request):
    CompletedTask.objects.all().delete()
    
    return redirect("home")