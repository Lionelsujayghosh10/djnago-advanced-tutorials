# Generated by Django 3.0.5 on 2020-04-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(null=True, upload_to='Images/student/', verbose_name='Image'),
        ),
    ]
