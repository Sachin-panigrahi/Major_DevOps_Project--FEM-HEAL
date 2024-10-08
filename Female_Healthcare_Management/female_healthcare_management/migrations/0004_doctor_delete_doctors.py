# Generated by Django 5.0.7 on 2024-07-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female_healthcare_management', '0003_alter_doctors_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.DeleteModel(
            name='Doctors',
        ),
    ]
