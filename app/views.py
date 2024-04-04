from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from .models import User, Question, Choice
from .forms import QuestionForm, ChoicesForm, AuthForm, ChangePasswordForm

def index(request):
    questions = Question.objects.filter(hidden=False)
    paginator = Paginator(questions, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {
        "user": request.user,
        "page_obj": page_obj
    })


def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            c1 = form.cleaned_data["choice1"]
            c2 = form.cleaned_data["choice2"]
            c3 = form.cleaned_data["choice3"]
            c4 = form.cleaned_data["choice4"]
            question = Question.objects.create(
                text=text,
                user=request.user
            )
            for c in [c1, c2, c3, c4]:
                if c != "":
                    Choice.objects.create(
                        text=c,
                        question=question
                    )
            return redirect("/")
    else:
        form = QuestionForm()
    return render(request, "new-question.html", {"form": form})


def question_detail(request, id):
    q = Question.objects.get(id=id)
    if request.method == "POST":
        form = ChoicesForm(q, request.POST)
        if form.is_valid():
            selected_id = int(form.cleaned_data["choice"])
            choice = Choice.objects.get(id=selected_id)
            choice.selected_count = choice.selected_count + 1
            choice.save()
            return redirect("/")
    else:
        form = ChoicesForm(q)
    return render(request, "question-detail.html", {
        "question": q,
        "form": form
    })


# auth views
def auth(request):
    login_form = AuthForm()
    register_form = AuthForm()
    return render(request, "auth/auth.html", {
        "login_form": login_form,
        "register_form": register_form
    })


def auth_login(request):
    form = AuthForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, messages.WARNING, "User Not Found")
            login_form = AuthForm()
            register_form = AuthForm()
            return render(request, "auth/auth.html", {
                "login_form": login_form,
                "register_form": register_form
            })

        login(request, user)
        return redirect("/")


def auth_register(request):
    form = AuthForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = User.objects.create_user(username, None, password)

        if user is None:
            messages.add_message(request, messages.WARNING, "Failed to create user")
            login_form = AuthForm()
            register_form = AuthForm()
            return render(request, "auth/auth.html", {
                "login_form": login_form,
                "register_form": register_form
            })

        login(request, user)
        return redirect("/")


def account(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, "auth/account.html", {
        "user": request.user,
        "questions": questions
    })


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data["old_password"]):
                request.user.set_password(form.cleaned_data["new_password"])
                request.user.save()
                login(request, request.user)
                messages.add_message(request, messages.SUCCESS, "Password changed successfully")
                return redirect("/account")
            else:
                messages.add_message(request, messages.ERROR, "Password incorrect")
                return redirect("/account")
    else:
        form = ChangePasswordForm()
    return render(request, "auth/change-password.html", {"form": form})



