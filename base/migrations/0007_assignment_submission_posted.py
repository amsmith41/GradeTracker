# Generated by Django 5.1.1 on 2024-12-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_assignment_is_submitted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='submission_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]