# Generated by Django 2.0.9 on 2020-01-23 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runnerapp', '0004_auto_20200123_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_1',
            old_name='table_1_user',
            new_name='writer',
        ),
        migrations.RenameField(
            model_name='table_2',
            old_name='table_2_user',
            new_name='writer',
        ),
        migrations.RenameField(
            model_name='table_3',
            old_name='table_2_user',
            new_name='writer',
        ),
        migrations.RenameField(
            model_name='table_4',
            old_name='table_4_user',
            new_name='writer',
        ),
    ]
