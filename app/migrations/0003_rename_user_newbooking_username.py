# Generated by Django 4.2.3 on 2023-08-18 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_newbooking_membername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newbooking',
            old_name='user',
            new_name='username',
        ),
    ]
