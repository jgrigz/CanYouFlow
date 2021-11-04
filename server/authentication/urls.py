from django.urls import path
from authentication import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("register/", auth_views.RegisterView.as_view(), name="signup"),
    path("logout/", auth_views.logout_view, name="logout"),

]