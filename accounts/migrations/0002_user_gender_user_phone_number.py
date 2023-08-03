# Generated by Django 4.2.4 on 2023-08-03 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("M", "남성"), ("F", "여성")], default="", max_length=1
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                default="",
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator("^010-?[1-9]\\d{3}-?\\d{4}$")
                ],
            ),
            preserve_default=False,
        ),
    ]
