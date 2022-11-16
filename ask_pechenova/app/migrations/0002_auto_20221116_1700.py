# Generated by Django 3.2.7 on 2022-11-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='answer_dislikes', to='app.Member'),
        ),
        migrations.AddField(
            model_name='answer',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='answer_likes', to='app.Member'),
        ),
        migrations.AddField(
            model_name='question',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='question_dislikes', to='app.Member'),
        ),
        migrations.AddField(
            model_name='question',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='question_likes', to='app.Member'),
        ),
    ]
