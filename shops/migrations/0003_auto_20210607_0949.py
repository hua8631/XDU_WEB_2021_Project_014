# Generated by Django 3.0.10 on 2021-06-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20210607_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='dis_price',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格'), max_digits=10, verbose_name='折扣价'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='是否可用'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='短标签'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日期'),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='活动')),
                ('slug', models.SlugField(max_length=200, verbose_name='短标签')),
                ('discount', models.IntegerField(default=100, verbose_name='折扣百分比')),
                ('available', models.BooleanField(default=True, verbose_name='是否可用')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
