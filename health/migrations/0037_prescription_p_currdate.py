# Generated by Django 3.2 on 2021-04-27 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0036_remove_prescription_p_currdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='p_currdate',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
