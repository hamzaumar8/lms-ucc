# Generated by Django 3.2 on 2021-08-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucclms', '0007_book_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
