# Generated by Django 3.2 on 2021-04-27 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0024_prescription_p_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='p_currdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
