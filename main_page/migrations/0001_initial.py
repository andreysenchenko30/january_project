# Generated by Django 3.1.5 on 2021-01-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Congratulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congratulation', models.CharField(max_length=255)),
            ],
        ),
    ]
