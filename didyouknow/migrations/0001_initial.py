# Generated by Django 2.0.13 on 2019-05-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curiosity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curiosityText', models.TextField(unique=True, verbose_name='User name')),
            ],
        ),
    ]
