from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import ImageCollectionPage


@login_required
def welcome(request):
    return render(request, 'collection/welcome_page.html', {'user': request.user})

def login_view(request):
    # Use Django's built-in authentication form
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    
    if request.method == 'POST':
        # Get the form data and authenticate the user
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                error_message = 'User not found'
                return render(request, 'registration/login.html', {'error_message': error_message})
        else:
            print(form.errors)
            print(form.fields)
            print(form.cleaned_data)
            print(form.as_p())
            raise ValueError("Invalid form")

    return render(request, 'registration/login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('welcome')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')