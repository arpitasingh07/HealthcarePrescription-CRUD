# Generated by Django 3.2 on 2021-04-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_alter_prescription_p_currdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='p_currdate',
            field=models.DateField(blank=True),
        ),
    ]
