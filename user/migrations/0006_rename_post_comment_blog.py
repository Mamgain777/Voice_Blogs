# Generated by Django 4.1 on 2023-03-12 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_comment_time"),
    ]

    operations = [
        migrations.RenameField(model_name="comment", old_name="post", new_name="blog",),
    ]
