# Generated by Django 3.1.1 on 2020-10-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_static_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='static',
            name='position',
            field=models.CharField(choices=[('about', 'about'), ('contact', 'contact')], max_length=20, unique=True),
        ),
    ]