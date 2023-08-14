# Generated by Django 4.2.3 on 2023-07-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyUser",
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
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("identifier", models.CharField(max_length=255, unique=True)),
                (
                    "identifier_type",
                    models.CharField(
                        choices=[
                            ("EMAIL", "Email"),
                            ("PHONE_NUMBER", "Phone number"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]