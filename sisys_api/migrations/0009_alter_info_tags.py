# Generated by Django 4.0.1 on 2022-11-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisys_api', '0008_alter_info_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='tags',
            field=models.ManyToManyField(blank=True, to='sisys_api.Tag'),
        ),
    ]
