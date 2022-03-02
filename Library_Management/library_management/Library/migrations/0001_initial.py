# Generated by Django 4.0.2 on 2022-02-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookTitle', models.CharField(max_length=1000)),
                ('Author', models.CharField(max_length=1000)),
                ('Publisher', models.CharField(max_length=1000)),
                ('Genre', models.CharField(max_length=1000)),
                ('Year', models.CharField(max_length=1000)),
                ('Language', models.CharField(max_length=1000)),
                ('Description', models.TextField()),
                ('Tags', models.CharField(max_length=1000)),
                ('ISBN', models.CharField(max_length=1000)),
            ],
        ),
    ]
