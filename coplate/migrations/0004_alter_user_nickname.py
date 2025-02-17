# Generated by Django 5.0.6 on 2024-05-24 14:37

import coplate.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coplate", "0003_user_nickname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="nickname",
            field=models.CharField(
                error_messages={"unique": "이미 사용중인 닉네임입니다."},
                max_length=15,
                null=True,
                unique=True,
                validators=[coplate.validators.validate_no_special_characters],
            ),
        ),
    ]
