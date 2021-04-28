from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Prescription
from django.contrib import messages
from health.forms import Patientforms



# Create your views here.

def showPatients(request):
    showall=Prescription.objects.all()
    return render(request,'home.html',{"data":showall})

def insertPatients(request):
    if request.method =='POST':
        if request.POST.get("p_name") and request.POST.get("p_id") and  request.POST.get("p_img") and  request.POST.get("p_contact") and  request.POST.get("p_dob") and  request.POST.get("p_age") and  request.POST.get("p_gender") and  request.POST.get("p_diagnosed") and request.POST.get("p_blood") and  request.POST.get("p_rate") and request.POST.get("p_height") and  request.POST.get("p_weight") and request.POST.get("p_allergies") and  request.POST.get("p_health") and  request.POST.get("p_city") and  request.POST.get("p_address") and request.POST.get("p_drug") and request.POST.get("p_unit") and  request.POST.get("p_dosage") and  request.POST.get("p_check") and  request.POST.get("present_date") :
            saverecord= Prescription()
            saverecord.p_name=request.POST.get('p_name')
            saverecord.p_id=request.POST.get('p_id')
            saverecord.p_img=request.POST.get('p_img')
            saverecord.p_contact=request.POST.get('p_contact')
            saverecord.p_dob=request.POST.get('p_dob')
            saverecord.p_age=request.POST.get('p_age')
            saverecord.p_gender=request.POST.get('p_gender')
            saverecord.p_diagnosed=request.POST.get('p_diagnosed')
            saverecord.p_blood=request.POST.get('p_blood')
            saverecord.p_rate=request.POST.get('p_rate')
            saverecord.p_height=request.POST.get('p_height')
            saverecord.p_weight=request.POST.get('p_weight')
            saverecord.p_allergies=request.POST.get('p_allergies')
            saverecord.p_health=request.POST.get('p_health')
            saverecord.p_city=request.POST.get('p_city')
            saverecord.p_address=request.POST.get('p_address')
            saverecord.p_drug=request.POST.get('p_drug')
            saverecord.p_unit=request.POST.get('p_unit')
            saverecord.p_dosage=request.POST.get('p_dosage')
            saverecord.p_check=request.POST.get('p_check')
            saverecord.present_date=request.POST.get('present_date')
            
            
         
           

            saverecord.save()
          
            return render(request,'base.html')
    else:
        return render(request,'base.html')

def editPatients(request,id):
    ed_tempobj=Prescription.objects.get(id=id)
    return render(request,'edit.html',{"Prescription": ed_tempobj})

def updatePatients(request,id):
    
        updateP=Prescription.objects.get(id=id)
        form=Patientforms(request.POST,instance=updateP)
        if form.is_valid():
            form.save()
            messages.success(request,'Record updated successfully!!')
            return render(request,'edit.html',{"Prescription": updateP})
        


def deletePatients(request,id):
    deleteP=Prescription.objects.get(id=id)
    deleteP.delete()
    showdata=Prescription.objects.all()
    return render(request,'home.html',{"data": showdata})










    

