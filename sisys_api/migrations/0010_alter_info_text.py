# Generated by Django 4.0.1 on 2022-11-09 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisys_api', '0009_alter_info_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='text',
            field=models.TextField(max_length=16384),
        ),
    ]