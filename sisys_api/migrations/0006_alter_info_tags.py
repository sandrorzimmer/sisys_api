# Generated by Django 4.0.1 on 2022-11-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisys_api', '0005_alter_info_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='tags',
            field=models.ManyToManyField(blank=True, limit_choices_to={'owner': 'sisys_api.UserProfile'}, to='sisys_api.Tag'),
        ),
    ]
