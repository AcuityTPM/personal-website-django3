# Generated by Django 3.0.6 on 2020-05-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tite', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
