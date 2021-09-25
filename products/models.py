from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PrintingMethod(models.Model):
    """
    A model for the printing methods.
    """
    PRINTING_METHOD = (
        ('one_sided', '4/0 CMYK'),
        ('double_sided', '4/4 CMYK')
    )

    name = models.CharField(max_length=50)
    method = models.CharField(
        choices=PRINTING_METHOD, max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    """
    A model for the available sizes.
    """
    SIZE = (
        ('a4', 'A4'),
        ('a5', 'A5'),
        ('a6', 'A6'),
        ('a0', 'A0'),
        ('a1', 'A1'),
        ('a2', 'A2'),
        ('standard', 'Standard'),
        ('double_v', 'Double V'),
        ('double_h', 'Double H'),
    )

    name = models.CharField(max_length=50)
    method = models.CharField(
        choices=SIZE, max_length=50)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    """
    A model for product tags with selectable Bootstrap colors.
    """
    PRODUCT_TAG = (
        ('danger', 'Red'),
        ('succes', 'Green'),
        ('primary', 'Blue'),
        ('warning', 'Yellow')
    )

    name = models.CharField(max_length=50)
    method = models.CharField(
        choices=PRODUCT_TAG, max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A model for the products.
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)
    method = models.ForeignKey(
        PrintingMethod, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(
        Size, null=True, on_delete=models.SET_NULL)
    product_tag = models.ForeignKey(
        ProductTag, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=500)
    delivery_time = models.IntegerField(default=5)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name