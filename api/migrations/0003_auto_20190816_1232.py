# Generated by Django 2.2.4 on 2019-08-16 07:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20190816_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='name',
            new_name='Course',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'Course')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'Course')},
        ),
    ]
