# Generated by Django 3.2 on 2021-04-27 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0016_remove_prescription_p_currdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='current',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
