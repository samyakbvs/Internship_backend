# Generated by Django 2.1 on 2020-01-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_auto_20200128_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Contains_docs',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='Contains_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='Contains_video',
            field=models.BooleanField(default=False),
        ),
    ]
