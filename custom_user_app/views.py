from django.shortcuts import render
from custom_user_app.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return render(request, "index.html")

def user_detail_view(request, user_id):
    user_detail = CustomUser.objects.get(id=user_id)
    return render(request, "user_detail.html", {"user_detail":user_detail })

def profile_view(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'user_profile.html', {'user': user})

def welcome_view(request):
    return render(request, "welcome.html")
