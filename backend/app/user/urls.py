from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("register", views.register, name="user_register"),
    path("login", views.user_login, name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
    path("profile", views.profile, name="user_profile"),
]
