# Generated by Django 4.2.6 on 2024-06-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phoneNo',
            field=models.CharField(max_length=10),
        ),
    ]
