# Generated by Django 2.2.6 on 2019-10-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='age',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='country',
        ),
        migrations.AddField(
            model_name='commodity',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]