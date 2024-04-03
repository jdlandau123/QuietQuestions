from django.contrib import admin
from .models import Question, Choice, User

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ["postedDate"]

admin.site.register(Choice)
admin.site.register(User)

