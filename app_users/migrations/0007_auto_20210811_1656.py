# Generated by Django 3.0.7 on 2021-08-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0006_auto_20210811_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_types',
            field=models.CharField(choices=[('lecturer', 'lecturer'), ('student', 'student')], max_length=10),
        ),
    ]
