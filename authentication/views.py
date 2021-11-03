from django.shortcuts import render, HttpResponseRedirect
from authentication.forms import LoginForm, SignUpForm
from custom_user_app.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View

# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST)
        return render(request, 'generic_form.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        breakpoint()
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                email =data.get("email"),
                password =data.get("password"),
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                request.GET.get("next", reverse("welcome"))
                )
        else:
            form = LoginForm()
        return render(request, "index.html", {"form":form})


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data["username"], 
                password=data["password"], 
                full_name=data["full_name"],
                email=data["email"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("home"))
                )
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

def password_reset_view(request):
    ...

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))