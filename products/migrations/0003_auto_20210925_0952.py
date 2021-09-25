# Generated by Django 3.2.6 on 2021-09-25 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('method', models.CharField(choices=[('one_sided', '4/0 CMYK Printed on one side'), ('double_sided', '4/4 CMYK Printed on both sides')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('method', models.CharField(choices=[('danger', 'Red'), ('succes', 'Green'), ('primary', 'Blue'), ('warning', 'Yellow')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('method', models.CharField(choices=[('a4', 'A4'), ('a5', 'A5'), ('a6', 'A6'), ('a0', 'A0'), ('a1', 'A1'), ('a2', 'A2'), ('standard', 'Standard, 85x55 mm'), ('double_v', 'Double V, 85x110 mm'), ('double_h', 'Double H, 170x55 mm')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_time',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='product',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.printingmethod'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.producttag'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.size'),
        ),
    ]