from django.shortcuts import render, redirect
from .forms import CustomUserFreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserFreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserFreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts_form.html', context)