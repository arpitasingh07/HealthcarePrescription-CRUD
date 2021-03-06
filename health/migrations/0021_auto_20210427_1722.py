# Generated by Django 3.2 on 2021-04-27 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_alter_prescription_p_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='p_id',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='p_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
    ]
