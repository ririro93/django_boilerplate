from django.shortcuts import render, redirect
from .forms import ProfileForm

# Create your views here.
def profile(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
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