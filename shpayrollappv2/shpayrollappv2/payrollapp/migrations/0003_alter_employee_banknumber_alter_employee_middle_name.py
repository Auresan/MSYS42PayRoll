# Generated by Django 5.0.3 on 2024-05-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0002_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='BankNumber',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
