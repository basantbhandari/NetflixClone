# Generated by Django 3.0.3 on 2020-09-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not available', max_length=40),
        ),
    ]