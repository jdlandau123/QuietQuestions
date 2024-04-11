from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    followed_questions = models.ManyToManyField("Question", related_name="followed_questions")


class Question(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField(blank=True, null=True)
    postedDate = models.DateField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-postedDate"]


class Choice(models.Model):
    text = models.TextField()
    selected_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)

