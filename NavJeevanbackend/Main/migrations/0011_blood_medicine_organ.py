# Generated by Django 5.0.1 on 2025-02-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_rename_doctor_title_doctor_doctor_name_patent_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=200)),
                ('blood_Avail', models.CharField(max_length=200)),
                ('blood_donars', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=200)),
                ('medicine_Avail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ_name', models.CharField(max_length=200)),
                ('organ_Avail', models.CharField(max_length=200)),
                ('organ_donars', models.CharField(max_length=200)),
            ],
        ),
    ]
