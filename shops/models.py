from typing import Any, Tuple

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator











# 功能主体models  Category and Product

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shops:product_list_by_category',
                         args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0, verbose_name='数量')
    name = models.CharField(max_length=200, db_index=True, verbose_name='名字')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='短标签')
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True, verbose_name='图片')
    description = models.TextField(blank=True, verbose_name='描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    available = models.BooleanField(default=True,verbose_name='是否可用')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建日期')
    updated = models.DateTimeField(auto_now=True,verbose_name='更新日期')


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shops:product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name






