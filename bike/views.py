from django.shortcuts import render
from .models import Bicicleta
from .forms import BicicletaForm

# Create your views here.
def index(request):
    return render(request,'bicicleta/index.html')

def bicicletas(request):
    return render(request,'bicicleta/bicicletas.html')

def iniciosesion(request):
    return render(request,'bicicleta/iniciosesion.html')

def registro(request):
    return render(request,'bicicleta/registro.html')

def home(request):
    ListaBicicletas = Bicicleta.objects.all()
    datos = {'bicicletas':ListaBicicletas}
    return render(request, 'bicicleta/index.html',datos)

def form_bicicleta(request):
    form = BicicletaForm()
    return render(request, 'bicicleta/form_bicicleta.html',{'form':form}) 