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
def ordine_details(request,pd,id):
    piatto=Piatti.objects.get(id=pd)
    context={"piatto":piatto,"id":id,"pd":pd}
    return render(request,'ordine_details.html',context=context)


def piatti_ordinati(request):
    id_preno=request.POST['prenot_id']
    id_piat = request.POST['piat_id']

    quant = request.POST['quantita']
    if quant:
        quantita=quant
    else:
        quantita=1
    piatto=Piatti.objects.get(id=id_piat)
    piatto.quantita=quantita
    ordini=Ordini()
    ordini.prenota=Prenotazione.objects.get(id=id_preno)
    ordini.piatto = piatto
    ordini.save()

    return redirect(reverse('ordine', args=(id_preno,)))

def tutti_prenotazione(request):
    prno=Prenotazione.objects.filter(user=request.user)
    return render(request,'tutti_pro.html',{"pro":prno})
def details(request,id):
    prenot=Prenotazione.objects.get(id=id)
    ord=Ordini.objects.filter(prenota=id)
    context={'ord': ord}
    context["name"]=prenot.user.username
    context["date"] = prenot.date
    context["time"] = prenot.time
    context["Npersone"] = prenot.number_of_persons
    return render(request,'details.html',context=context)