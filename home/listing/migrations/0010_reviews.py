# Generated by Django 3.1.1 on 2020-10-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_auto_20201007_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('review', models.TextField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
