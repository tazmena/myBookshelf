# Generated by Django 4.1.5 on 2023-04-29 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_usertoread'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserToRead',
        ),
    ]
