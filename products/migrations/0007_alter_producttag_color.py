# Generated by Django 3.2.6 on 2021-09-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210925_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttag',
            name='color',
            field=models.CharField(choices=[('danger', 'Red'), ('success', 'Green'), ('primary', 'Blue'), ('warning', 'Yellow')], max_length=50),
        ),
    ]