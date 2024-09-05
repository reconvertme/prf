from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Formulaire personnalisé
from .forms import SignUpForm

# Inscription
def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)  # Personnalisé
        # form = UserCreationForm(request.POST) 
        if form.is_valid():
            # form.save()                # Sauvegarde en DB
            login(request, form.save())  # Inscription et login en même temps
            return redirect("journaux_list")
    else:
        form = SignUpForm() # Formulaire personnalisé
        # form = UserCreationForm() # Formulaire vide

    return render(request, 'users/register.html', {"form":form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())           # Login the user
            return redirect("journal-create")
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            #     return redirect("journal-create")
            
    else:
        form = AuthenticationForm() # Formulaire vide

    return render(request, 'users/login.html', {"form":form})

# Logout
def logout_view(request):
    if request.method == "POST":
        logout(request)  # Logout
        return redirect("journaux:home")
