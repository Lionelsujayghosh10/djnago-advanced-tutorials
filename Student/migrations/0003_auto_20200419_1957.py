# Generated by Django 3.0.5 on 2020-04-19 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20200418_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll_numer',
            new_name='roll_number',
        ),
    ]
