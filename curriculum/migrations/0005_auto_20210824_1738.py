# Generated by Django 3.0.7 on 2021-08-24 16:38

import curriculum.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20210824_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='Assignment',
            field=models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Assignment'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='Notes',
            field=models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Course code'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='ppt',
            field=models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Presentations'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_body',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='standard',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='standard',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=curriculum.models.save_subject_image, verbose_name='Subject Image'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
