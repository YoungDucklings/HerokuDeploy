# Generated by Django 2.2.4 on 2019-11-27 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='cast',
            order_with_respect_to='movie',
        ),
    ]
