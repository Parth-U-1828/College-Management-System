from django.shortcuts import render
from .models import DeptModel,StudentModel
from .forms import DeptForm,StudentForm

def home(request):
	return render(request,"home.html")

def showdept(request):
	data = DeptModel.objects.all()
	return render(request,"showdept.html",{"data":data})

def adddept(request):
	if request.method == "POST":
		data = DeptForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "Department created"
			fm = DeptForm()
			return render(request,"adddept.html",{"fm":fm,"msg":msg})
		else:
			msg = "Check Errors"
			fm = DeptForm()
			return render(request,"adddept.html",{"fm":data,"msg":msg})
	else:
		fm = DeptForm()
		return render(request,"adddept.html",{"fm":fm})

def removedept(request,id):
	dt = DeptModel.objects.get(did=id)
	dt.delete
	return redirect("showdept")

def showstudent(request):
	data = StudentModel.objects.all()
	return render(request,"showstudent.html",{"data":data})

def addstudent(request):
	if request.method == "POST":
		data = StudentForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "Student Created"
			fm = StudentForm()
			return render(request,"addstudent.html",{"fm":fm,"msg":msg})
		else:
			msg = "Check Errors"
			fm = StudentForm()
			return render(request,"addstudent.html",{"fm":data,"msg":msg})
	else:
		fm = StudentForm()
		return render(request,"addstudent.html",{"fm":fm})

def removestudent(request,id):
	dt = StudentModel.objects.get(rno=id)
	dt.delete()
	return redirect("showstudent")


	




















			
