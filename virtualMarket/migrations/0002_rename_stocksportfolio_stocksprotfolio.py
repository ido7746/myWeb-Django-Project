# Generated by Django 3.2.6 on 2021-09-10 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtualMarket', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StocksPortfolio',
            new_name='StocksProtfolio',
        ),
    ]