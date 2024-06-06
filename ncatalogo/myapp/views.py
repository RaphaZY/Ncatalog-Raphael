from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET":
        return render(request, 'site/cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        
        if user:
            messages.error(request, "Usuari já existe")
            return render(request, "site/.html")
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect(login)


def login(request):
    if request.method == "GET":
        return render(request, "site/index.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:

            login_django(request, user)
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect(index)
        
        else:
            messages.error(request, "Nome ou senha invalidos")
            return redirect(index)
        
def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário Deslogado!')
    return redirect(login)



def index(request):
    produtos = Roupa.objects.all()
    return render(request, 'site/index.html', {"itens": produtos})



@login_required
def create(request):
    form = RoupaForm
    if request.method == "POST":
        form = RoupaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "site/cadastro_item.html", {"forms":form})


@login_required
def edit(request, id):
    item = Roupa.objects.get(pk=id)
    form = RoupaForm(instance=item)
    return render(request, "site/update.html",{"form":form, "item":item})

@login_required
def update(request, id):
    try:
        if request.method == "POST":
            item = Roupa.objects.get(pk=id)
            form = RoupaForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')

@login_required
def read(request, id):
    item = Roupa.objects.get(pk=id)
    return render(request, "site/read.html", {"item": item})


@login_required
def all(request):
    return render(request, "site/lista.html", {"itens": Roupa.objects.all()})



@login_required
def delete(request, id):
    item = Roupa.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

