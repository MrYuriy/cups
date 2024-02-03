# Generated by Django 5.0.1 on 2024-02-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_company', models.CharField(max_length=100)),
                ('shop', models.CharField(max_length=3)),
                ('user', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=8)),
                ('identifier', models.CharField(max_length=12)),
                ('print_status', models.BooleanField(default=False)),
            ],
        ),
    ]
