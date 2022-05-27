from django.shortcuts import render, redirect
from . import models
from . import forms
from django.db import connection
from datetime import datetime

def index(request):
	return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def register(request):
    msg=''
    if request.method=='POST':
        form=forms.CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Thanks for the registration.'
    form=forms.CompanyForm
    return render(request, 'register.html',{'form':form,'msg':msg})

def login(request):
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        company=models.Companies.objects.filter(username=username,password=password).count()
        if company > 0:
            company=models.Companies.objects.filter(username=username,password=password).first()
            request.session['companyLogin']=True
            request.session['company_id']=company.id
            return redirect('/dashboard')
        else:
            msg='Login Failed! Please enter valid details.'
    form=forms.CompanyLoginForm
    return render(request, 'login.html',{'form':form,'msg':msg})

def logout(request):
    del request.session['companyLogin']
    return redirect('/login')

def dashboard(request):
	return render(request, 'dashboard.html')

def admin_login(request):
    msg=''
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        company=models.Admins.objects.filter(username=username,password=password).count()
        if company > 0:
            company=models.Admins.objects.filter(username=username,password=password).first()
            request.session['adminLogin']=True
            request.session['admin_id']=company.id
            return redirect('/admin_dashboard')
        else:
            msg='Login Failed! Please enter valid details.'
    form=forms.AdminsLoginForm
    return render(request, 'admin/login.html',{'form':form,'msg':msg})

def admin_logout(request):
    del request.session['adminLogin']
    return redirect('/admin_login')

def admin_dashboard(request):
	return render(request, 'admin/dashboard.html')

def add_tender(request):
    company_id=request.session['company_id']
    msg=''
    if request.method=='POST':
        form=forms.TenderForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Tender added successfully.'
    form=forms.TenderForm
    return render(request, 'add_tender.html',{'form':form,'msg':msg,'company_id':company_id})

def my_tenders(request):  
    company_id=request.session['company_id']
    tenders = models.Tenders.objects.raw("SELECT a.*, b.company_name, b.company_phone FROM tenders as a LEFT JOIN companies as b ON a.company_id = b.id WHERE a.company_id = "+str(company_id));
    return render(request,"my_tenders.html",{'tenders':tenders})

def edit_tender(request, id):
    company_id=request.session['company_id']
    msg=''
    if request.method=='POST':
        tender = models.Tenders.objects.get(id=id)
        form=forms.TenderForm(request.POST, instance=tender)
        if form.is_valid():
            form.save()
            msg='Tender updated successfully.'
    tender = models.Tenders.objects.get(id=id)
    form=forms.TenderForm(instance=tender) 
    return render(request, 'edit_tender.html',{'form':form,'msg':msg,'tender':tender,'company_id':company_id})

def tenders(request):  
    today = datetime.today()
    #todays_date = datetime.today().strftime('%Y-%m-%d')
    #WHERE a.tender_close_date >= '"+todays_date+"'
    tenders = models.Tenders.objects.raw("SELECT a.*, b.company_name, b.company_phone FROM tenders as a LEFT JOIN companies as b ON a.company_id = b.id ORDER BY a.id DESC");
    return render(request,"tenders.html",{'tenders':tenders,'today':today})

def apply_to_tender(request, tender_id):
    tender = models.Tenders.objects.get(id=tender_id)
    msg=''
    if request.method=='POST':
        form=forms.TenderApplyForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Applied to tender successfully.'
    form=forms.TenderApplyForm
    return render(request, "apply_to_tender.html",{'form':form,'tender_id':tender_id,'tender':tender,'msg':msg})

def applied_to_tender(request,tender_id):
    tender_appliers =models.TenderAppliers.objects.filter(tender_id=tender_id).all()
    return render(request, "applied_to_tender.html", {'tender_appliers':tender_appliers})

def give_tender(request, tender_id, id):  
    if request.method == "GET":
        models.TenderAppliers.objects.filter(tender_id=tender_id).all().update(given_to=0)
        tender_applier = models.TenderAppliers.objects.get(id=id)
        tender_applier.given_to = 1    
        tender_applier.save()
    return redirect("/applied_to_tender/"+str(tender_id))	

def companies(request):
    companies =models.Companies.objects.all()
    return render(request, "admin/companies.html", {'companies':companies})