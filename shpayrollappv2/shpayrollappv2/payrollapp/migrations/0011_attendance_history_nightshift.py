# Generated by Django 5.0.3 on 2024-05-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0010_alter_hmo_hmo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_history',
            name='NightShift',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
