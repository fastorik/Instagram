# Generated by Django 4.0.3 on 2022-05-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='tag',
            field=models.CharField(max_length=255),
        ),
    ]
