# Generated by Django 5.1.1 on 2024-11-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_course_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='instruction',
            field=models.TextField(default='Here are the instructions for the assignment!'),
        ),
    ]