# Generated by Django 5.0.2 on 2024-03-03 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='title',
        ),
    ]
