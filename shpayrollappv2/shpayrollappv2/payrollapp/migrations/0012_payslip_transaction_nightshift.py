# Generated by Django 5.0.3 on 2024-05-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0011_attendance_history_nightshift'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip_transaction',
            name='NightShift',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]