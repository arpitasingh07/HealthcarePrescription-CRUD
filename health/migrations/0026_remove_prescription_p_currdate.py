# Generated by Django 3.2 on 2021-04-27 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0025_prescription_p_currdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='p_currdate',
        ),
    ]
