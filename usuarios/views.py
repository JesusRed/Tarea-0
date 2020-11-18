from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from usuarios.decorators import unauthenticated_user
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth import login
# from django.views.generic.base import TemplateView
# from django.views.generic.edit import FormView
# from django.contrib.auth.views import LoginView    
from .models import Usuario
from pqrs.models import Pqrs
from .forms import UserForm,FormularioLogin
from django.contrib import messages

# from usuarios.forms import CreateUserForm
# from .forms import User
# Create your views here.

# class Login(FormView):
#     template_name='usuarios/login.html'
#     form_class = FormularioLogin
#     success_url = reverse_lazy('login')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return redirect(self.get_success_url())
#         else:
#             return super(Login,self).dispatch(request,*args,**kwargs) 

#     def form_valid(self,form):
#         login(self.request, form.get_user())
#         return super(Login,self).form_valid(form)


def registrarUsuario(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        # name = form.cleaned_data.get('name')
        if form.is_valid():
               usuario= form.save()
               messages.success(request, 'Cuenta creada ')
            
               return redirect('misPqr')
    context = {'form': form}
    return render(request, 'usuarios/register.html', context)



def loginUsuario(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        usuario= authenticate(request,email=email , password=password)
        print(email)
        print(password)
        # if usuario is not None:
        login(request,usuario)
        print('AQUI')
        return redirect('newPqr')
        
    else:
        messages.info(request,'Email o contraseña incorrecta')
    context={}
    print('NO ENTRO')
    return render(request,'usuarios/login.html')


def misPqr(request):
    pqrs=Pqrs.objects.all()
    return render(request,'usuarios/mispqr.html',{'pqrs':pqrs})

