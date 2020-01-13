# Generated by Django 3.0.2 on 2020-01-13 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_auto_20200113_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowance_name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='allowances',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payroll.Allowance'),
        ),
    ]
