from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.
def cadastro(request):
    return render(request, 'polls/login.html', {})

def test(request):
    return render(request, 'polls/test.html', {})



def login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        #login(request, user)
        # Redirect to a success page.
        return render(request, 'polls/login.html', {})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'polls/test.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return render(request, 'polls/login.html', {})
            
    else:
        form = UserForm()
    return render(request, 'polls/signup.html', {})
        