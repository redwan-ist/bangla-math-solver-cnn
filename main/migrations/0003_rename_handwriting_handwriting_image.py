# Generated by Django 4.0.4 on 2022-05-17 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_handwriting_delete_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handwriting',
            old_name='handwriting',
            new_name='image',
        ),
    ]
