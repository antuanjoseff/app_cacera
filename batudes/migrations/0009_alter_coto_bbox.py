# Generated by Django 5.0.4 on 2024-04-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batudes', '0008_coto_bbox_alter_coto_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coto',
            name='bbox',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
