from django.contrib import admin
from products.models import Product, Category, Image

from django.utils.html import mark_safe


class ProductInline(admin.TabularInline ,admin.StackedInline):
    model = Image
    extra = 1
    verbose_name_plural = 'Images'
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('id','name','category','price','quantity',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)
