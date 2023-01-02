from django.shortcuts import render,redirect
from crud.models import Employees

# Create your views here.
def index(request):
    emp =Employees.objects.all()

    context ={
        'emp':emp,

    }
    return render(request,'index.html',context)


def ADD(request):
    if request.method == 'POST':
        name= request.POST.get('name'),
        email= request.POST.get('email'),
        address=request.POST.get('address'),
        phone = request.POST.get('phone'),

        emp= Employees(
            name = name,
            email = email,
            address = address,
            phone = phone,

        )
        emp.save()
        return redirect('index')

    return render(request,'index.html')


def Edit(request):
    emp=Employees.objects.all()

    context ={
        'emp':emp,
    }
    return redirect(request,'index.html',context)


def Update(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,

        )
        emp.save()
        return redirect('index')


    return redirect(request,'index.html')


def Delete(request):
    emp = Employees.objects.filter(id = id)
    emp.delete()


    context={
        'emp':emp,

    }
    return redirect('index')



