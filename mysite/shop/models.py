from typing import Any, Tuple

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator




class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class GOODS(models.Model):
    def __str__(self):
        return self.question_text

    ID = models.AutoField()



class AdministratorManager(BaseUserManager):
    """
    定义一个返回所有管理员用户的ModelManager(is_superuser=True)，通过调用__call__方法返回所有超级用户
    """
    def __call__(self):
        return self.model._default_manager.filter(is_superuser=True)

    def random(self):
        from random import choice
        return choice(list(self.__call__()))

    def reset_password(self, password):
        pass

class NickNameSubstitution(models.base.ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
        if attrs.get('username', False):
            username = attrs.pop('username')
            new_class = super_new(cls, name, bases, attrs, **kwargs)
            new_class.__dict__.update(**{new_class.USERNAME_FIELD: username})
            return new_class
        else:
            new_class = super_new(cls, name, bases, attrs, **kwargs)
            for base in bases:
                if hasattr(base, 'username'):
                    username = getattr(base, 'username', None)
                    setattr(new_class, new_class.USERNAME_FIELD, username)
                    return new_class


def get_user_or_anonymous(request, require_previleges=False, **kwargs):
    """
    Django request对象带有user属性指向当前用户，来自未登录用户的请求指向AnonymousUser
    :param request: request对象
    :param require_previleges: 对于需要登录的页面，设置require_previleges=True则返回request.user, 后续由视图来处理业务逻辑
    :param kwargs: 视图匹配到的参数, 例如nick_name
    :return: User对象
    """
    if require_previleges:
        return request.user
    if kwargs.get('nick_name'):
        return User.objects.get(nick_name=kwargs.get('nick_name'))
    # fall back to session user
    return request.user or None




class User(AbstractUser):
    """
    fields inherited from AbstractUser:
    - email
    - date_joined
    """
    USERNAME_FIELD = 'nick_name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    default_manager = UserManager()
    username = None
    # 允许昵称重复,而使用email登录
    nick_name = models.CharField(
        verbose_name=_('Nick Name'), max_length=50, null=False, blank=True,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=False, null=False, unique=False)
    # 用户头像
    avatar = models.ImageField(verbose_name="avatar", upload_to="avatar/%Y/%m/%d", default="avatar/default_avatar.png")
    hover_image = models.ImageField(verbose_name='blog hover', upload_to='hover_imgs/%Y/%m/%d',
                                    default='hover_imgs/default_hover_image.png', null=True, blank=True)
    signature = models.TextField(verbose_name=_('signature'), max_length=500, null=True, blank=True)

    # model managers, default manager is objects
    administrators = AdministratorManager()


    def get_nick_name_display(self):
        if not self.nick_name:
            return self.__class__.objects.normalize_email(self.email)
        name = self.__class__.normalize_username(self.nick_name)
        return name






# 功能主体models  Category and Product

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                         args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name






