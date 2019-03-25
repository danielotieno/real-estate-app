from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        pass
        # Register User
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        pass
        # Login User
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('index')
