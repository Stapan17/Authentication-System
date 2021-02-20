from django.shortcuts import render, redirect
from .models import User, infoUser
from .forms import infoUserForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    registered = False
    context = {'registered': registered}
    return render(request, 'base.html', context)


def reg(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_info_form = infoUserForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            registered = True
            context = {'registered': registered, 'user': user}
            return render(request, 'base.html', context)

        else:
            registered = False
            context = {'registered': registered,
                       'user_form.errors': user_form.errors, 'user_info_form.errors': user_info_form.errors}
            return render(request, 'base.html', context)
    else:

        user_form = UserForm()
        user_info_form = infoUserForm()

        registered = False
        context = {'user_form': user_form,
                   'user_info_form': user_info_form, 'registered': registered}

        return render(request, 'reg.html', context)


def log(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            registered = True
            context = {'registered': registered}
            return render(request, 'base.html', context)

        else:
            return redirect('log')

    return render(request, 'login.html')


@login_required
def log_out(request):
    logout(request)
    registered = False
    context = {'registered': registered}
    return render(request, 'base.html', context)
