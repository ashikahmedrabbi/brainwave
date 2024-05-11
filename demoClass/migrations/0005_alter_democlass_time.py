# Generated by Django 5.0.1 on 2024-05-11 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoClass', '0004_rename_class_status_democlass_classstatus_and_more'),
        ('teacher', '0003_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='democlass',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.availabletime'),
        ),
    ]
