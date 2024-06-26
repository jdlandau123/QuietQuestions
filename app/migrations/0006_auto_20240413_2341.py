# Generated by Django 5.0.3 on 2024-04-13 23:41

from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model("app", "Category")
    cat_names = [
        "Advice",
        "Relationships",
        "Family",
        "Work",
        "School",
        "Hobbies",
        "Just For Fun",
        "Other"
    ]

    for cat in cat_names:
        Category.objects.create(name=cat)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_question_categories'),
    ]

    operations = [
        migrations.RunPython(create_categories, migrations.RunPython.noop)
    ]
