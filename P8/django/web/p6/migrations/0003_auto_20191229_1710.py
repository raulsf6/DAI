# Generated by Django 2.2.7 on 2019-12-29 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p6', '0002_auto_20191229_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='lat',
            new_name='birthplace_latitude',
        ),
        migrations.RenameField(
            model_name='musician',
            old_name='lon',
            new_name='birthplace_longitude',
        ),
    ]