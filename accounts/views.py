from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user permissions
            if user.is_superuser:
                return redirect('secretary')  # URL name for secretary dashboard
            elif user.is_staff:
                return redirect('finance')  # URL name for finance dashboard
            elif user.is_active:
                return redirect('president')  # URL name for president dashboard
            else:
                messages.error(request, 'You do not have permission to access this system.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('home1')  
