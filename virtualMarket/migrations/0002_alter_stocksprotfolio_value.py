# Generated by Django 3.2.6 on 2021-09-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualMarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocksprotfolio',
            name='value',
            field=models.FloatField(default=1),
        ),
    ]