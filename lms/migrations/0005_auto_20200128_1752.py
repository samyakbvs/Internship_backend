# Generated by Django 2.1 on 2020-01-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_auto_20200128_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Doc',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
