# Generated by Django 3.0.3 on 2020-09-05 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='StudentRegistration',
        ),
    ]