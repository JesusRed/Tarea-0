from django.shortcuts import render

# Create your views here.
    
def informacion(request):
    return render(request,"core/infosoli.html")
