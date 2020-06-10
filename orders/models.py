from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField()
    phon = models.CharField(max_length=11, verbose_name='Телефон', default='')
    dostavka = models.CharField(max_length=250, default='', verbose_name='Способ доставки')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданный')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновленный')
    paid = models.BooleanField(default=False, verbose_name='Оплаченный')
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='Приказ')
    product = models.ForeignKey(Product, related_name='order_items', verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
# Create your models here.
