# Generated by Django 2.2.4 on 2021-02-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_publisher_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='descripcion',
            field=models.TextField(default='old'),
            preserve_default=False,
        ),
    ]
