# Generated by Django 3.1.1 on 2020-10-08 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
