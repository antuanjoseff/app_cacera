# Generated by Django 5.0.4 on 2024-04-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batudes', '0010_alter_coto_bbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coto',
            name='bbox',
            field=models.CharField(blank=True, default=0, max_length=255),
            preserve_default=False,
        ),
    ]