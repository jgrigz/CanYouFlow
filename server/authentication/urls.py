from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from authentication.views import CreateCustomUser, CustomUsersView


#  using regex so it will ONLY work at localhost 5000
url_patterns = [
    path("cyf-register/", CreateCustomUser.as_view()),
    path("cyf-all-users/", CustomUsersView.as_view())
]