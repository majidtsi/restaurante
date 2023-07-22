from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from .form import PrenotaForm
from .models import Piatti, Prenotazione, Ordini


# Create your views here.
def index(request):
    cat=Piatti.objects.all()
    context={'piat':cat}
    return render(request,'index.html',context=context)

def logout(request):
    logout(request)
    return redirect(reverse(''))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def prenota(request):
    if request.method=='POST':
        form = PrenotaForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            user=request.user
            myform.user=user
            myform.save()
            my=myform.id
            p=Prenotazione.objects.get(id=my)
            print(p)


            return redirect(reverse('ordine',args=(my, )))

    else:
        print("nooooo")
        form1 = PrenotaForm()

    return render(request,'prenota.html',{'form':form1})

def ordine(request,id):
    piatti=Piatti.objects.all()


    return render(request,'ordine.html',{"id":id,"piatti":piatti})

def piatti_ordinati(request):
    id_preno=request.POST['prenot_id']
    id_piat = request.POST['piat_id']
    ordini=Ordini()
    ordini.prenota=Prenotazione.objects.get(id=id_preno)
    ordini.piatto = Piatti.objects.get(id=id_piat)
    ordini.save()
    return redirect(reverse('ordine', args=(id_preno,)))

def tutti_prenotazione(request):
    prno=Prenotazione.objects.filter(user=request.user)
    return render(request,'tutti_pro.html',{"pro":prno})
def details(request,id):
    prenot=Prenotazione.objects.get(id=id)
    print(prenot)
    print("----------")
    ord=Ordini.objects.filter(prenota=prenot)
    print(ord)
    return render(request,'details.html',{'ord':ord})