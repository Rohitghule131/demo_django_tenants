# Generated by Django 4.2 on 2023-10-15 16:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customeuser', '0003_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
