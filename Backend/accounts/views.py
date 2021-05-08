from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def profile(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(instance=user, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = ProfileForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/profile.html', context)
    else:
        return redirect('account_login')

def change_pw(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_pw.html', context)