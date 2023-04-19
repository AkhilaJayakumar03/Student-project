from django.contrib import messages
from django.shortcuts import render
from.forms import *
from.models import *


# Create your views here.
def student(request):
    if request.method=='POST':
        a=student_form(request.POST)
        if a.is_valid():
            sn=a.cleaned_data['student_name']
            db=a.cleaned_data['date_of_birth']
            pm=a.cleaned_data['physics_mark']
            cm=a.cleaned_data['chemistry_mark']
            mm=a.cleaned_data['maths_mark']
            cs=a.cleaned_data['computer_science_mark']
            b=student_model(student_name=sn,date_of_birth=db,physics_mark=pm,chemistry_mark=cm,maths_mark=mm,computer_science_mark=cs)
            b.save()
            messages.success(request,"Registration success")
        else:
            messages.success(request,"Registration failed")
    return render(request,"student_register.html")

def studentdetail(request):
    a=student_model.objects.all()
    stnm=[]
    dtbh=[]
    phmk=[]
    chmk=[]
    msmk=[]
    csmk=[]
    tt=[]
    for i in a:
        sn=i.student_name
        stnm.append(sn)
        dt=i.date_of_birth
        dtbh.append(dt)
        pm=i.physics_mark
        phmk.append(pm)
        cm=i.chemistry_mark
        chmk.append(cm)
        ms=i.maths_mark
        msmk.append(ms)
        cs=i.computer_science_mark
        csmk.append(cs)
        total_mark = pm + cm + ms + cs
        total_per = str((total_mark / 400) * 100)
        tt.append(total_per)
    mylist=zip(stnm,dtbh,phmk,chmk,msmk,csmk,tt)
    return render(request, "student_detail.html", {'mylist':mylist})
