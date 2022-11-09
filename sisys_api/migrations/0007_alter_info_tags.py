# Generated by Django 4.0.1 on 2022-11-05 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sisys_api', '0006_alter_info_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'owner': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)}, to='sisys_api.Tag'),
        ),
    ]
