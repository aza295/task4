from django.db import models

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField('Title',max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'PRODUCT'
        verbose_name_plural = 'Продукты'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
