# Generated by Django 3.2 on 2021-04-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_alter_prescription_p_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='p_check',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
