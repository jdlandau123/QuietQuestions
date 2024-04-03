from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
    pass


class Question(models.Model):
    text = models.TextField()
    postedDate = models.DateField(auto_now_add=True)
    hidden = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)


class Choice(models.Model):
    text = models.TextField()
    selected_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)

