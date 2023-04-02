from django.urls import path

from core import views


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("inbox/", views.inbox, name="inbox"),
    path("dashboard/", views.dashboard, name="dashboard"),
]