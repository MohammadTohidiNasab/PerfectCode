# Generated by Django 4.1.6 on 2023-02-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0003_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(null=True, verbose_name="عنوان"),
        ),
    ]
