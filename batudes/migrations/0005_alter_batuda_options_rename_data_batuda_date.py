# Generated by Django 5.0.4 on 2024-04-16 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batudes', '0004_alter_batuda_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batuda',
            options={'ordering': ('date',), 'verbose_name_plural': 'Batudes'},
        ),
        migrations.RenameField(
            model_name='batuda',
            old_name='data',
            new_name='date',
        ),
    ]