# Generated by Django 2.2.1 on 2019-05-31 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190531_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]