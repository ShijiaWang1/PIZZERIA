# Generated by Django 3.0.5 on 2022-05-06 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_topping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='text',
            new_name='pizza_name',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topic',
            new_name='Pizza',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='text',
            new_name='topping_name',
        ),
    ]
