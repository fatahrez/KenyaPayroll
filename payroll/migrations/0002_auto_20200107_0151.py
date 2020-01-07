# Generated by Django 3.0.2 on 2020-01-07 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='contract_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='date_of_employment',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='employee_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='employee_job_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='job_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='mobile_phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
