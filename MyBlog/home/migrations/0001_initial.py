# Generated by Django 3.0.6 on 2020-05-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField(max_length=400)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
