# Generated by Django 4.2 on 2023-10-15 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customeuser', '0005_remove_customuser_uuid_customuser_user_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_uuid',
            new_name='id',
        ),
    ]
