# Generated by Django 3.2.13 on 2022-06-02 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20220601_0420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='ven_id',
            new_name='ven',
        ),
    ]
