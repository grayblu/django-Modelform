from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form 이 저장되고, user session 을 create 한다.
            user = form.save()            
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    content = { 'form': form, }
    return render(request, 'accounts/auth_form.html', content)


def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # user session create
            return redirect(request.GET.get('next') or 'boards:index')
            # http://127.0.0.1:8000/accounts/login/?next=/boards/create/ 에서
            # next 는 key
    else:
        form = AuthenticationForm()

    content = { 'form': form, }
    return render(request, 'accounts/auth_form.html', content)


def logout(request):
    auth_logout(request)
    return redirect('boards:index')


def delete(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('boards:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 현재 사용자의 인증 세션이 무효화 되는 것을 막고, 세션을 유지
            update_session_auth_hash(request, user)
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    context ={ 'form': form,}
    return render(request, 'accounts/auth_form.html', context)