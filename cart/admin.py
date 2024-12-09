from django.contrib import admin
from cart.models import Cart, CartProduct
from products.models import Product

class ProductInline(admin.TabularInline ,admin.StackedInline):
    model = CartProduct
    extra = 1
    verbose_name_plural = 'Products'
    
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('id','get_cart_number', 'user')
    
    def get_cart_number(self, obj):
        return f"Cart {obj.pk}"
    get_cart_number.short_description = 'Cart Name'

admin.site.register(Cart, CartAdmin)

    
    

