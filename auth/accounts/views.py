from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUsercreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUsercreationForm()

    context = {
        'form':form,
    }


    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')


            return redirect(next_url or 'articles:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')