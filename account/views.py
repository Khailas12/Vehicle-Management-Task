from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from vehicle import models
from django.views.decorators.csrf import ensure_csrf_cookie


from . import forms


def index(request):
    return render(request, 'multi_user/index.html')


@ensure_csrf_cookie
def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('login_user')

        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form = forms.SignUpForm()

    context = {'form': form}
    return render(request, 'multi_user/register.html', context)


@never_cache
def login_user(request):
    form = forms.LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_super_admin:
                login(request, user)
                return redirect('super_admin_page')

            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_page')

            elif user is not None and user.is_user:
                login(request, user)
                return redirect('user_page')

            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {'form': form}
    return render(request, 'multi_user/login.html', context)


@login_required(login_url='login_user')
def super_admin_page(request):
    context = {}
    context['dataset'] = models.VehicleModel.objects.all()
    return render(request, 'multi_user/super_admin_page.html', context)


@login_required(login_url='login_user')
def admin_page(request):
    context =  {}
    context['dataset'] = models.VehicleModel.objects.all()
    return render(request, 'multi_user/admin_page.html', context)


@login_required(login_url='login_user')
def user_page(request):
    context =  {}
    context['dataset'] = models.VehicleModel.objects.all()
    return render(request, 'multi_user/user_page.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login_user')
