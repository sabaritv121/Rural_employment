# Generated by Django 4.2.10 on 2024-03-20 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_appointmentschedule_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentschedule',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
