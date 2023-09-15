from django.shortcuts import render
from backend.models import Carausel

# Create your views here.
def beranda(request):
    carausel = Carausel.objects.all()
    context ={
        'title':'BEranda | Jasaizin.id',
        'carausel':carausel
    }
    return render(request,'beranda/beranda.html',context)