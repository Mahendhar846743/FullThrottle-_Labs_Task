# Generated by Django 2.2.4 on 2020-03-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20200328_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_periods',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
