# Generated by Django 5.0.3 on 2024-04-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-postedDate']},
        ),
        migrations.AddField(
            model_name='user',
            name='followed_questions',
            field=models.ManyToManyField(related_name='followed_questions', to='app.question'),
        ),
    ]
