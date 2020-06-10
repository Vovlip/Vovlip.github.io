from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['Логин'], password=cd['Пароль'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
def index(request):
    return render(request, 'account/index.html', {'section': 'dashboard'})
def kontakt(request):
    return render(request, 'account/kontakt.html', {'section': 'dashboard'})
def onas(request):
    return render(request, 'account/onas.html', {'section': 'dashboard'})
def dostavka_oplata(request):
    return render(request, 'account/dostavka_oplata.html', {'section': 'dashboard'})
# Create your views here.
