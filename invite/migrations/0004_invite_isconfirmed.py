# Generated by Django 3.0.2 on 2020-01-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0003_auto_20191201_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='isConfirmed',
            field=models.BooleanField(default=False),
        ),
    ]