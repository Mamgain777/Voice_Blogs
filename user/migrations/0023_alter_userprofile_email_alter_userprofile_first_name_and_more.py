# Generated by Django 4.1 on 2023-03-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0022_alter_userprofile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images/profile"),
        ),
    ]
