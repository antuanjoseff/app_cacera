# Generated by Django 5.0.4 on 2024-04-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batudes', '0002_alter_batuda_options_coto_short_code_alter_coto_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coto',
            name='code',
        ),
    ]
