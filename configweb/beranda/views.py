from django.shortcuts import render

# Create your views here.
def beranda(request):
    context ={
        'title':'BEranda | Jasaizin.id'
    }
    return render(request,'beranda/beranda.html',context)