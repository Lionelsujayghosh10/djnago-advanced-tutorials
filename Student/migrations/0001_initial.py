# Generated by Django 3.0.5 on 2020-04-17 19:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClassSection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=255)),
                ('student_code', models.CharField(max_length=100)),
                ('roll_numer', models.IntegerField()),
                ('student_image', models.CharField(max_length=155)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stduent_class', to='ClassSection.Classes')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_section', to='ClassSection.Section')),
            ],
            options={
                'db_table': 'report_card_student',
            },
        ),
    ]
