# Generated by Django 4.0 on 2022-02-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(default=0)),
                ('ven_id', models.IntegerField(default=0)),
                ('statusOn', models.BooleanField(default=True)),
            ],
        ),
    ]
