# Generated by Django 4.1 on 2023-03-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0016_alter_blog_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="snippet",
            field=models.TextField(default="Testing", max_length=100),
        ),
    ]
