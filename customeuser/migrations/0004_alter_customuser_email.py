# Generated by Django 4.2 on 2023-07-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customeuser', '0003_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email address is already associated with another account.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]