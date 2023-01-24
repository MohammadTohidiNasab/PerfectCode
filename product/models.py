from django.db import models
from category.models import Category
from django.utils.translation import gettext as _
# Create your models here.

#product model
class Product(models.Model):
    name = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=250)
    price = models.CharField(_("قیمت"), max_length=50)
    stock = models.IntegerField(_("تعداد موجود"), default=0)
    is_active = models.BooleanField(_("فعال"), default=True, blank=True)
    image = models.ImageField(_("تصویر"), upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان به روز رسانی"), auto_now=True)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'


#comment model
class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100) 
    email = models.EmailField(_("ادرس الکترونیکی"), max_length=254)        
    massage = models.TextField(_("متن نظر"))
    date = models.DateField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    def __str__(self):
       return self.email
            
    class Meta:
        verbose_name = ' نظر '
        verbose_name_plural = ' نظرات '
