# Generated by Django 4.0.4 on 2022-05-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handwriting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handwriting', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]