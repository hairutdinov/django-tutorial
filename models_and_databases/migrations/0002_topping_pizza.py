# Generated by Django 4.2.5 on 2023-11-26 06:54
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("models_and_databases", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topping",
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
                ("name", models.CharField()),
            ],
            options={
                "db_table": '"topping"',
            },
        ),
        migrations.CreateModel(
            name="Pizza",
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
                ("name", models.CharField()),
                ("toppings", models.ManyToManyField(to="models_and_databases.topping")),
            ],
            options={
                "db_table": '"pizza"',
            },
        ),
    ]