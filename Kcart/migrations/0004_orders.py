# Generated by Django 3.0.4 on 2020-08-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kcart', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.IntegerField(max_length=15)),
                ('additional_phone', models.IntegerField(max_length=15)),
            ],
        ),
    ]
