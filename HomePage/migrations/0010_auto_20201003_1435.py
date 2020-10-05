# Generated by Django 3.1.2 on 2020-10-03 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomePage', '0009_auto_20201003_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='alias',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='link',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]