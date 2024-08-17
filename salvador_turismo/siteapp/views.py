from django.shortcuts import render

def home (request):
    return render(request,'index.html')

def atracoes (request):
    return render(request,'atracoes.html') 

def historia (request):
    return render(request, 'historia.html')
