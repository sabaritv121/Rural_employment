# Generated by Django 4.2.10 on 2024-03-20 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_appointmentschedule_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentschedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='emp_app.panchayath'),
        ),
    ]
