# Generated by Django 5.0.6 on 2024-05-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_path', models.CharField(blank=True, max_length=128)),
                ('stock', models.IntegerField(default=0)),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
