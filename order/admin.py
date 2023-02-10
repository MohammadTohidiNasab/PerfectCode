from django.contrib import admin
from .models import Ordering
# Register your models here.

class OrderingAdmin(admin.ModelAdmin):
    fields = ('user',('product_names','total_products'),'created_at','updated_at')
    readonly_fields = ('updated_at','created_at')
    list_display = ('user','transaction_id','created_at','updated_at','product_names','total_products')
    save_on_top = True
admin.site.register(Ordering,OrderingAdmin)