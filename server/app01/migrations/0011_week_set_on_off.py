# Generated by Django 4.1.3 on 2022-12-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_week_set_pref'),
    ]

    operations = [
        migrations.AddField(
            model_name='week_set',
            name='on_off',
            field=models.IntegerField(default=0),
        ),
    ]