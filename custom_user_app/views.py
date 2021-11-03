from django.shortcuts import render
from custom_user_app.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View


def index_view(request):
    return render(request, "index.html")


class WelcomeView(View, LoginRequiredMixin):
    """homepage for app"""

    def get(self, request):

        template = "welcome.html"
        logged_in_user = request.user
        context = {"logged_in_user": logged_in_user}
        return render(request, template, context)

    def post(self, request):
        ...


class UserDetailView(View):
    """individual user profile by id"""

    def get(self, request, id):

        target_user = CustomUser.objects.get(id=id)
        template = "user_detail.html"
        context = {"target_user": target_user}
        return render(request, template, context)

    def post(self, request, id):
        ...
