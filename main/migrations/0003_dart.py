# Generated by Django 3.1.3 on 2022-04-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220420_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]