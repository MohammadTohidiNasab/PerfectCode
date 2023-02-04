from django.contrib import admin
from .models import Product 
# Register your models here.


admin.site.site_header = 'پنل مدیریت سایت'
admin.site.site_title ='مدیریت'
admin.site.index_title = 'درگاه مدیریت سایت فروشگاه'


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('created_at',)
    filter_horizontal = ()
    list_display = ('name','price','created_at','color','stock')
    list_editable = ('price','stock')
    
    
admin.site.register(Product,ProductAdmin)
