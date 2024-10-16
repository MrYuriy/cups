# Generated by Django 4.1.13 on 2024-10-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("label", "0005_labelstock"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="labelstock",
            name="comment",
        ),
        migrations.RemoveField(
            model_name="labelstock",
            name="deskription",
        ),
        migrations.RemoveField(
            model_name="labelstock",
            name="sku",
        ),
        migrations.AddField(
            model_name="labelstock",
            name="delivery_part",
            field=models.CharField(blank=True, default="", max_length=12, null=True),
        ),
        migrations.AddField(
            model_name="labelstock",
            name="lines_info",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
