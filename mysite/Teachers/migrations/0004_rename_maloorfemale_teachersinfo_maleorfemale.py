# Generated by Django 5.0.1 on 2024-01-21 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0003_alter_teachersinfo_contracttype_delete_contracttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachersinfo',
            old_name='maloOrFemale',
            new_name='maleOrFemale',
        ),
    ]
