# Generated by Django 4.2.4 on 2023-08-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='Book on life', max_length=250),
            preserve_default=False,
        ),
    ]
