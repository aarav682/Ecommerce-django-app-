# Generated by Django 3.0.4 on 2020-08-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kcart', '0010_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
