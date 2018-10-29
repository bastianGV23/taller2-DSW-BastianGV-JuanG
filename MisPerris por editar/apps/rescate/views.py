from django.shortcuts import render,redirect
from .models import perrito
from apps.rescate.forms import formServicio
# Create your views here.
def lista_rescate(request):
    rescata = perrito.objects.all()
    return render(request, "rescate/rescate.html",{'rescata':rescata})

def crea_rescate(request):
    form = formServicio(request.POST, request.FILES or None)
    
    if form.is_valid():
      form.save()
      return redirect('index')
    else:
        form = formServicio()
    
    context =  {
        'form': form,
    }
    return render(request,'rescate/nuevo.html',context)
