# Generated by Django 5.0.4 on 2024-04-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batudes', '0009_alter_coto_bbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coto',
            name='bbox',
            field=models.CharField(max_length=255, null=True),
        ),
    ]