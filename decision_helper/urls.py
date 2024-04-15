from django.contrib import admin
from django.urls import path, include
from app.views import auth, index, account, new_question, question_detail, \
    change_password, auth_login, auth_register, question_results, following, \
    search, report, confirmation, contact, about, category
from django.contrib.auth import views as auth_views
from rest_framework import routers
from app.api import QuestionViewSet

api_router = routers.DefaultRouter()
api_router.register("questions", QuestionViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("ask/", new_question, name="new question"),
    path("questions/<int:id>", question_detail, name="question detail"),
    path("questions/<int:id>/results", question_results, name="question results"),
    path("questions/<int:id>/report", report, name="report question"),
    path("category/<str:name>", category, name="category"),
    path("following", following, name="following"),
    path("search", search, name="search"),
    path("confirmation", confirmation, name="confirmation"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("auth/", auth, name="auth"),
    path("login/", auth_login, name="login"),
    path("register/", auth_register, name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("account/", account, name="account"),
    path("account/change_password", change_password, name="change password"),
    path("api/", include(api_router.urls)),
    path("admin/", admin.site.urls),
]
