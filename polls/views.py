from django.shortcuts import render
from django.contrib.auth import authenticate, login

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
        return render(request, 'polls/test.html', {})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'polls/login.html', {})
        