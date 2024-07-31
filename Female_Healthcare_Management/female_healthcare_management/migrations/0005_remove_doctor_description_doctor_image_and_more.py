# Generated by Django 5.0.7 on 2024-07-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female_healthcare_management', '0004_doctor_delete_doctors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='description',
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to='doctor_images/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(max_length=100),
        ),
    ]
