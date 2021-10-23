# Generated by Django 3.2.6 on 2021-10-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]