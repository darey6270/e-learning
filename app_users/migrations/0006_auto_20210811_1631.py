# Generated by Django 3.0.7 on 2021-08-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_auto_20210809_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_types',
            field=models.CharField(choices=[('lecturer', 'lecturer'), ('student', 'student')], default='student', max_length=10),
        ),
    ]