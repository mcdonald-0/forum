# Generated by Django 4.0.2 on 2022-02-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_question_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]