# Generated by Django 4.1 on 2022-08-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
