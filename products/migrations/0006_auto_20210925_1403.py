# Generated by Django 3.2.6 on 2021-09-25 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210925_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='producttag',
            old_name='method',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='method',
            new_name='size',
        ),
    ]
