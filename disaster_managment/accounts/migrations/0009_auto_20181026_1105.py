# Generated by Django 2.1.2 on 2018-10-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20181026_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='Name',
            new_name='username',
        ),
    ]