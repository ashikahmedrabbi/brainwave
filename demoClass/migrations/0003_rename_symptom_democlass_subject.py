# Generated by Django 5.0.1 on 2024-03-30 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoClass', '0002_rename_appointment_democlass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='democlass',
            old_name='symptom',
            new_name='Subject',
        ),
    ]
