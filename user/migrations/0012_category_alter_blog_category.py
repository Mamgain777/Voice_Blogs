# Generated by Django 4.1 on 2023-03-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0011_blog_category_alter_blog_title_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="blog", name="category", field=models.CharField(max_length=40),
        ),
    ]
