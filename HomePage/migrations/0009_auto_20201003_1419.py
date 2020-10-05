# Generated by Django 3.1.2 on 2020-10-03 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import random


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomePage', '0008_auto_20201003_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='creator',
            field=models.ForeignKey(default=random.Random.randint, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]