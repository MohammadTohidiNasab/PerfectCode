from django.db import models
from category.models import Category
from account.models import User
from django.utils.translation import gettext as _
# Create your models here.

#product model
class Product(models.Model):
    name = models.CharField(_("عنوان"), max_length=50,null=True)
    description = models.CharField(_("توضیحات"), max_length=250,null=True)
    price = models.CharField(_("قیمت"), max_length=50,null=True)
    stock = models.IntegerField(_("تعداد موجود"), default=0 ,null=True)
    color = models.CharField(_("رنگ"), max_length=50,null=True)
    is_active = models.BooleanField(_("فعال"), default=True, blank=True ,null=True)
    image = models.ImageField(_("تصویر"), upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True ,null=True)
    updated_at = models.DateTimeField(_("زمان به روز رسانی"), auto_now=True,null=True)
    category  = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True,null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'


#comment model
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100,null=True) 
    email = models.EmailField(_("ادرس الکترونیکی"), max_length=254,null=True)        
    massage = models.TextField(_("متن نظر"),null=True)
    date = models.DateField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True,null=True)
    def __str__(self):
       return self.email
            
    class Meta:
        verbose_name = ' نظر '
        verbose_name_plural = ' نظرات '
