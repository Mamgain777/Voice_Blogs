# Generated by Django 4.1 on 2023-03-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_comment_options_alter_comment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment", name="author", field=models.TextField(max_length=30),
        ),
    ]
