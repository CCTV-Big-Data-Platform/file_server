# Generated by Django 3.0.6 on 2020-06-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=100)),
                ('userToken', models.CharField(max_length=500)),
            ],
        ),
    ]