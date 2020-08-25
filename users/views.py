from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your account has been created successfully! You can log in")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
