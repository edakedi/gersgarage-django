# Generated by Django 3.2.6 on 2021-08-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50)),
                ('engine_type', models.CharField(blank=True, max_length=50)),
                ('make', models.CharField(blank=True, max_length=50)),
                ('licence_detail', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
