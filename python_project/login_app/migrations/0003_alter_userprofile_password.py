# Generated by Django 4.1.1 on 2022-10-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_userprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
