from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.id} | {self.title}'

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField()
    info = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.title}'

    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'products'