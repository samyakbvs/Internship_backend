# Generated by Django 3.0.3 on 2020-04-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_auto_20200128_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Init_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]