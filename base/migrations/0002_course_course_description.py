# Generated by Django 5.1.1 on 2024-11-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(default='No description available'),
        ),
    ]
