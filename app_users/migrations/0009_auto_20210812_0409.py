# Generated by Django 3.0.7 on 2021-08-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0008_auto_20210812_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user_types',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('student', 'student'), ('lecturer', 'lecturer')], default='student', max_length=10),
        ),
    ]
