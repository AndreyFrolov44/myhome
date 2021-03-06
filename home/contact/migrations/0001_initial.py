# Generated by Django 3.1.1 on 2020-10-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('address', 'address'), ('phone', 'phone'), ('email', 'email')], max_length=100)),
                ('svg', models.FileField(upload_to='contact')),
            ],
        ),
    ]
