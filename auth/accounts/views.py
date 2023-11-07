from django.shortcuts import render, redirect
from .forms import CustomUsercreationForm

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