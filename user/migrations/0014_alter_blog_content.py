# Generated by Django 4.1 on 2023-03-16 14:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0013_blog_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
