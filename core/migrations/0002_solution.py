# Generated by Django 3.0.8 on 2020-08-12 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft', models.CharField(max_length=30)),
                ('body', models.TextField()),
            ],
        ),
    ]
