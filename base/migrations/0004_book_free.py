# Generated by Django 4.1 on 2022-08-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rents'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='free',
            field=models.BooleanField(null=True),
        ),
    ]
