# Generated by Django 3.0.7 on 2021-08-12 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0009_auto_20210812_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('student', 'student'), ('lecturer', 'lecturer')], max_length=10),
        ),
    ]
