# Generated by Django 3.1.3 on 2022-04-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220426_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
    ]