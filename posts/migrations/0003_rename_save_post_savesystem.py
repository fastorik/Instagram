# Generated by Django 4.0.3 on 2022-05-23 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_likes_alter_post_save'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='save',
            new_name='saveSystem',
        ),
    ]
