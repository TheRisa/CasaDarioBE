# Generated by Django 2.0.13 on 2019-05-12 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_auto_20190512_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterteinment',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entertainment.EnterteinmentType', verbose_name='tipo'),
        ),
    ]
