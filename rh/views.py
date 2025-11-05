from django.shortcuts import render
from .models import Funcionarios

# Create your views here.
def home(request):
    return render(request,'home.html')
def produtos(request):
    return render(request,'produtos.html')
def clientes(request):
    return render(request,'clientes.html')
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)
   