# Generated by Django 4.1.5 on 2023-04-29 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_delete_usertoread'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookstoread', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]