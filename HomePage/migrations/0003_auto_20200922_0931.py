# Generated by Django 3.1.1 on 2020-09-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_auto_20200922_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='link',
            name='visitors',
            field=models.IntegerField(default=0),
        ),
    ]
