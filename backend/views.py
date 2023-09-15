from django.shortcuts import render, redirect
from django.contrib import messages
from backend.forms import FormCarausel
from backend.models import Carausel
# Create your views here

def dashborad(request):
    context ={
        'title':'Dashboard'
    }
    return render(request,'backend/dashboard.html',context)

    
def carausel(request):
    if request.POST:
        form = FormCarausel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil Menambahkan Carausel')
            form = FormCarausel()
            carausel = Carausel.objects.all() 
            context ={
                'title':'Carausel',
                'form':form,
                'carausel':carausel
            }
            return render(request,'backend/carausel.html',context)
    else:
        form =FormCarausel()
        carausel = Carausel.objects.all()
        return render(request,'backend/carausel.html',{'form':form,'carausel':carausel})

        
def editcaruasel(request, id_carausel):
    carausel = Carausel.objects.get(id =id_carausel)
    if request.POST:
        form = FormCarausel(request.POST, request.FILES, instance=carausel)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil di update')
            return redirect('editcarausel', id_carausel=id_carausel) 
    else:
        form =FormCarausel(instance=carausel)
        context ={
            'form':form,
            'carausel':carausel
        }
        return render(request,'backend/editcarausel.html',context)
    
    
def deletecarausel(request,id_carausel):
    carausel = Carausel.objects.get(id=id_carausel)
    carausel.delete()
    messages.success(request,'Berhasil dihapus')
    return redirect('carausel')

