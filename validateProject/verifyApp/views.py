from django.shortcuts import render, redirect
from .models import User, infoUser
from .forms import infoUserForm, UserForm, infoUserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy


def home(request):
    registered = False
    context = {'registered': registered}
    return render(request, 'base.html', context)


@login_required(login_url='log')
def index(request):
    registered = True

    current_user = request.user
    current_user_info = infoUser.objects.get(user_id=current_user.id)

    context = {'registered': registered, 'current_user': current_user,
               'current_user_info': current_user_info}
    return render(request, 'index.html', context)


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

            return redirect('index')

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
            return redirect('index')

        else:
            return redirect('log')

    return render(request, 'login.html')


@login_required
def log_out(request):
    logout(request)
    registered = False
    context = {'registered': registered}
    return render(request, 'base.html', context)


def update(request, pk):

    Object = infoUser.objects.get(user_id=pk)
    user_info_form = infoUserUpdateForm(instance=Object)

    if request.POST:
        form = infoUserUpdateForm(
            request.POST, request.FILES, instance=Object)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            user_info_form = obj

            return redirect('index')

    form = infoUserUpdateForm(
        instance=Object
    )

    context = {'form': form, 'Object': Object}
    return render(request, 'update.html', context)
