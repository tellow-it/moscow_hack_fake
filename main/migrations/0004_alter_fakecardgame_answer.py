# Generated by Django 4.0.5 on 2022-06-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_fakenews_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakecardgame',
            name='answer',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
