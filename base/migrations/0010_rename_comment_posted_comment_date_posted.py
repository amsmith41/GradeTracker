# Generated by Django 5.1.1 on 2024-12-05 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_comment_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_posted',
            new_name='date_posted',
        ),
    ]