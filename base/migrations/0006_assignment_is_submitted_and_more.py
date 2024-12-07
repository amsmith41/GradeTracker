# Generated by Django 5.1.1 on 2024-12-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_assignment_submitted_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='submitted_response',
            field=models.TextField(blank=True, null=True),
        ),
    ]