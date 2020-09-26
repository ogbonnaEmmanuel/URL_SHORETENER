from django.contrib.auth import logout
from django.shortcuts import render, redirect

from HomePage.forms import SignUpForm


def home(request):
    return render(request, 'profile.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('home')
