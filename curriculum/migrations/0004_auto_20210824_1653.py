# Generated by Django 3.0.7 on 2021-08-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_lesson_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(max_length=100),
        ),
    ]
