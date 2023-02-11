from django.contrib import admin
from .models import Product ,Comment
# Register your models here.


admin.site.site_header = 'پنل مدیریت سایت'
admin.site.site_title ='مدیریت'
admin.site.index_title = 'درگاه مدیریت سایت فروشگاه'


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter =('category',)
    ordering = ('created_at',)
    filter_horizontal = ()
    list_display = ('name','price','is_active','color','stock')
    list_editable = ('price','stock','is_active')


#costum actions
    def change_to_unavailable(self,request,queryset):
        for req in queryset:
            req.is_active = False
            req.save()
        self.message_user(request,'انجام شد')

    change_to_unavailable.short_descriptions = 'ناموجود شدند'
    actions = ('change_to_unavailable',)


admin.site.register(Product,ProductAdmin)

admin.site.register(Comment)