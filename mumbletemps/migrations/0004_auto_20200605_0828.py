# Generated by Django 2.2.12 on 2020-06-05 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mumbletemps", "0003_auto_20200604_1020"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tempuser",
            old_name="user_name",
            new_name="username",
        ),
    ]
