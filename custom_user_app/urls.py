from django.urls import path
from custom_user_app import views as custom_user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', custom_user_views.index_view, name='index'),
    path('home/', custom_user_views.WelcomeView.as_view(), name='home'),
    path("user_detail/<int:id>/", custom_user_views.UserDetailView.as_view(), name="user_detail"),
    path("all_users/", custom_user_views.AllUsersView.as_view(), name="all_users"),

]