# Generated by Django 5.0.1 on 2024-05-06 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoClass', '0003_rename_symptom_democlass_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='democlass',
            old_name='class_status',
            new_name='classStatus',
        ),
        migrations.RenameField(
            model_name='democlass',
            old_name='class_types',
            new_name='classTypes',
        ),
        migrations.RenameField(
            model_name='democlass',
            old_name='Subject',
            new_name='subject',
        ),
    ]