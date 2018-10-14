# Generated by Django 2.1.1 on 2018-10-13 22:04

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181013_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=70, unique=True, validators=[api.models.validate_portfolio_name]),
        ),
    ]
