# Generated by Django 4.0.5 on 2022-06-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_fakecardgame_answer_alter_fakenews_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakenews',
            name='correct',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]