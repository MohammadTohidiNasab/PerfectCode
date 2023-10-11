# Generated by Django 4.1.4 on 2023-01-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Otp",
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
                ("phone", models.CharField(max_length=11)),
                ("code", models.SmallIntegerField()),
                ("expiration_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
