# Generated by Django 4.1.5 on 2023-01-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_otp"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "کاربر", "verbose_name_plural": "کاربرها"},
        ),
        migrations.AddField(
            model_name="otp",
            name="token",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
