from django.shortcuts import render
from custom_user_app.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View

import speech_recognition as sr


def index_view(request):
    return render(request, "index.html")


# TODO:
'''
Creating boolean listening inside welcome view
set to False by default, in which the button 
on the template will set listening to True, 
which will activate the listener method. 
Listening will need to be called inside 
post method, which will redirect to home with 
audio passed from listner. 
'''
class WelcomeView(View, LoginRequiredMixin):
    """homepage for app"""

    listening = False

    def listener():
        '''listens to users voice and will save as audio'''
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Say Something Into The Mic')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print(f'You said:\n{text}')
            except Exception as err:
                print('Sorry I did not understand.\nError: [ {err} ]')
                text = None

        return text


    def get(self, request):

        template = "welcome.html"
        logged_in_user = request.user
        audio = "This-Will-Be-The-Response-From-Speech-Recognition"
        context = {"logged_in_user": logged_in_user, "audio": audio}
        return render(request, template, context)

    def post(self, request):
        ...


class AllUsersView(View):
    """display all active users"""

    def get(self, request):

        all_users = CustomUser.objects.all()
        template = "all_users.html"
        context = {"all_users": all_users}
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
