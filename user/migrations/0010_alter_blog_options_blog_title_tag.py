# Generated by Django 4.1 on 2023-03-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_alter_comment_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog", options={"ordering": ["-publish_date"]},
        ),
        migrations.AddField(
            model_name="blog",
            name="title_tag",
            field=models.CharField(default="#testing", max_length=50),
        ),
    ]
