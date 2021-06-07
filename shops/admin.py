from django.contrib import admin

# Register your models here.
from .models import Category, Product,Activity
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Activity)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount', 'available','created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['discount', 'available']
    prepopulated_fields = {'slug': ('name',)}


