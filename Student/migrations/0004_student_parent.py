# Generated by Django 3.0.5 on 2020-04-24 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parent', '0001_initial'),
        ('Student', '0003_auto_20200419_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='Parent.Parent'),
        ),
    ]