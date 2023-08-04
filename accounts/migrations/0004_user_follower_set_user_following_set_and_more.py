# Generated by Django 4.2.4 on 2023-08-04 10:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_avatar_alter_user_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="follower_set",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="user",
            name="following_set",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요.",
                upload_to="accounts/avatar/%Y/%m/%d",
            ),
        ),
    ]
