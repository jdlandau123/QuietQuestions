from django.contrib import admin
from .models import Question, Choice, User
from guardian.admin import GuardedModelAdmin

@admin.register(Question)
class QuestionAdmin(GuardedModelAdmin):
    readonly_fields = ["postedDate"]

admin.site.register(Choice)
admin.site.register(User)

