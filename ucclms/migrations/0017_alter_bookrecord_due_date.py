# Generated by Django 3.2.6 on 2021-10-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucclms', '0016_alter_bookrecord_date_of_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
