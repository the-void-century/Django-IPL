# Generated by Django 4.2.2 on 2023-06-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_alter_matches_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='dimissal_kind',
            field=models.CharField(default='', max_length=100),
        ),
    ]
