# Generated by Django 4.0.5 on 2022-07-05 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_warrenty'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
