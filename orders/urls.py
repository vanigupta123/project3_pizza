from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("user", views.user, name="user"),
    path("logout", views.logout_view, name="logout"),
    path("order", views.order, name="order")
]
