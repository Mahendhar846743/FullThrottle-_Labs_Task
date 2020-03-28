# Generated by Django 2.2.4 on 2020-03-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_periods',
            name='end_time',
            field=models.DateTimeField(verbose_name='Mar 28 2020 03:25PM'),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='start_time',
            field=models.DateTimeField(verbose_name='Mar 28 2020 03:25PM'),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='task.User'),
        ),
    ]