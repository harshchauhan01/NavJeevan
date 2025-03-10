# Generated by Django 5.0.1 on 2025-02-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_rename_medicine_donars_medicine_medicine_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=50)),
                ('billing_date', models.DateField()),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medicines', models.JSONField(default=list)),
            ],
        ),
    ]
