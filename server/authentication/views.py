from django.shortcuts import redirect, render, HttpResponseRedirect
from authentication.forms import LoginForm, RegisterForm
from custom_user_app.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View


class LoginView(View):
    '''login existing user'''

    def get(self, request):
        template = 'generic_form.html'
        form = LoginForm()
        context = {'form': form}
        return render(request, template, context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username =data.get("username"),
                password =data.get("password"),
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')


class RegisterView(View):
    '''create a new user'''

    def get(self, request):
        template = 'generic_form.html'
        form = RegisterForm()
        context = {'form': form}
        return render(request, template, context)

    def post(self, request):    
        form = RegisterForm(request.POST)
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
                return redirect('login')
        else:
            print('Form is not valid')
            return redirect('register')

def password_reset_view(request):
    ...

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))