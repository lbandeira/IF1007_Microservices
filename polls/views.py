from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .models import equipamento
from django.db.models import Q

# Create your views here.
def cadastro(request):
    return render(request, 'polls/login.html', {})

def test(request):
    return render(request, 'polls/test.html', {})



def login_user(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'polls/test.html', {})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'polls/login.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('equipamento_list')
            
    else:
        form = UserForm()
    return render(request, 'polls/signup.html', {})


def equipamento_list(request):
    equipamentos = equipamento.objects.all()
    context = {
       'equipamento_list': equipamentos
    }
    return render(request, 'polls/equipamento_list.html', context)


def SearchResultsView(request):
    model = equipamento
    query = self.request.GET.get('q')
    object_list = equipamento.objects.filter(
        Q(nome_equipamento__icontains=query) | Q(categoria_equipamento__icontains=query)
    )
    context = {
        'equipamento_list': object_list
    }
    return render(request, 'polls/equipamento_list.html', context)