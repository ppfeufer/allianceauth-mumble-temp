# Generated by Django 3.1.1 on 2020-09-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mumbletemps", "0005_tempuser_templink"),
    ]

    operations = [
        migrations.AddField(
            model_name="tempuser",
            name="character_id",
            field=models.IntegerField(default=0),
        ),
    ]
