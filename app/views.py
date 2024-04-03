from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Question, Choice
from .forms import QuestionForm, ChoicesForm

def index(request):
    questions = Question.objects.all().order_by("-postedDate")
    return render(request, "index.html", {
        "user": request.user,
        "questions": questions
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
def login_view(request):
    if request.method == "POST":
        if "username_login" in request.POST:
            username = request.POST["username_login"]
            password = request.POST["password_login"]
            user = authenticate(request, username=username, password=password)
        else:
            username = request.POST["username_register"]
            password = request.POST["password_register"]
            user = User.objects.create_user(username, None, password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.WARNING, "User Not Found")
    return render(request, "auth/login.html", {})


def account(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, "auth/account.html", {
        "user": request.user,
        "questions": questions
    })



