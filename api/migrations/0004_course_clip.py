# Generated by Django 2.2.4 on 2019-08-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190816_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='clip',
            field=models.FileField(null=True, upload_to='user_video/'),
        ),
    ]