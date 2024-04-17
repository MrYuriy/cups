# Generated by Django 4.1.13 on 2024-04-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("label", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="label",
            name="comment",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="label",
            name="data",
            field=models.CharField(default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="label",
            name="identifier",
            field=models.CharField(default="", max_length=12),
        ),
        migrations.AlterField(
            model_name="label",
            name="order",
            field=models.CharField(default="", max_length=8),
        ),
        migrations.AlterField(
            model_name="label",
            name="shop",
            field=models.CharField(default="", max_length=3),
        ),
        migrations.AlterField(
            model_name="label",
            name="user",
            field=models.CharField(default="", max_length=50),
        ),
    ]