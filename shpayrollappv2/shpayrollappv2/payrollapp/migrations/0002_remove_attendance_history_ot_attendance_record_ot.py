# Generated by Django 5.0.3 on 2024-04-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance_history',
            name='OT',
        ),
        migrations.AddField(
            model_name='attendance_record',
            name='OT',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
