# Generated by Django 4.2.1 on 2023-05-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
