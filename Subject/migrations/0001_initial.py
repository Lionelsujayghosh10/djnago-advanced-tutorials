# Generated by Django 3.0.5 on 2020-04-11 14:24

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
            name='Subject',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'report_card_subject',
            },
        ),
        migrations.CreateModel(
            name='AssignSubject',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('assign_subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('assign_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='ClassSection.Classes')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='ClassSection.Section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='Subject.Subject')),
            ],
            options={
                'db_table': 'report_card_assign_subject',
            },
        ),
    ]
