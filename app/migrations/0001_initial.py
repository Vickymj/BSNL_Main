# Generated by Django 4.2.4 on 2023-08-04 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=120)),
                ('fathername', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=100)),
                ('moblieno', models.CharField(max_length=100)),
                ('alternateno', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('panno', models.CharField(max_length=100)),
                ('aadhhaarno', models.CharField(max_length=100)),
                ('nomieename', models.CharField(max_length=100)),
                ('nomieeage', models.CharField(max_length=100)),
                ('nomieerelationship', models.CharField(max_length=100)),
                ('nomieeaddress', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('downpayment', models.CharField(max_length=100)),
                ('siterefer', models.CharField(max_length=100)),
                ('modeofpay', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('chequeno', models.CharField(max_length=100)),
                ('paydate', models.DateField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('seniorityno', models.CharField(max_length=100)),
                ('amno', models.CharField(max_length=100)),
                ('receiptno', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'newbook',
            },
        ),
    ]
