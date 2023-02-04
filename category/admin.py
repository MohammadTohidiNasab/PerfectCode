from django.contrib import admin
from . models import Category
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('slug','created_at')

    

admin.site.register(Category,CategoryAdmin)