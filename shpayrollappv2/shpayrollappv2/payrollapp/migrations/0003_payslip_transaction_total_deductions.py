# Generated by Django 5.0.3 on 2024-04-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0002_attendance_history_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip_transaction',
            name='Total_Deductions',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
