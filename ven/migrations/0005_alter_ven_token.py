# Generated by Django 3.2.13 on 2022-06-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ven', '0004_alter_ven_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ven',
            name='token',
            field=models.CharField(default='6UMIALEG', max_length=80),
        ),
    ]
