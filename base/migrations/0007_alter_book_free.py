# Generated by Django 4.1 on 2022-08-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_returns_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='free',
            field=models.BooleanField(default='True', null=True),
        ),
    ]
