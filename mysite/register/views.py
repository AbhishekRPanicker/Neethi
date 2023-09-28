from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Info
from .forms import CreateUserForm
from home.views import home
#from home.models import Legal_prof

# VIEWS
def register(request):
        if request.user.is_authenticated:
                print("yes")
                return redirect('/home')
        else:
                form = CreateUserForm()
                if request.method == 'POST':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        b = form.cleaned_data.get('bio')
                        ph = form.cleaned_data.get('phone')
                        occ = form.cleaned_data.get('occupation')
                        Info.objects.create(
                            user = User.objects.all().get(username=username),
                            bio = b,
                            phone = ph,
                            occupation = occ,
                        )

                        messages.success(request,'Account created successfully!')

                        return redirect('login')

                return render(request, "register/register.html", {'form':form})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                messages.info(request, 'Username or password is incorrect')
                        
        return render(request, 'register/register.html', {})