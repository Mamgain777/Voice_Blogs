# Generated by Django 4.1 on 2023-03-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0021_userprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=models.ImageField(blank=True, upload_to="images/profile"),
        ),
    ]
