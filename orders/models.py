from django.db import models
from shops.models import Product
class Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='姓氏')
    last_name = models.CharField(max_length=50,verbose_name='名字')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=250,verbose_name='地址')
    postal_code = models.CharField(max_length=20,verbose_name='邮编')
    city = models.CharField(max_length=100,verbose_name='城市')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    paid = models.BooleanField(default=False,verbose_name='是否支付')
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())




class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                                related_name='items',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                    on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity