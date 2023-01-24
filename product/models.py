from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Product(models.Model):
    name = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=250)
    price = models.CharField(_("قیمت"), max_length=50)
    stock = models.IntegerField(_("تعداد موجود"), default=0)
    is_active = models.BooleanField(_("فعال"), default=True, blank=True)
    image = models.ImageField(_("تصویر"), upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان به روز رسانی"), auto_now=True)
    '''ToDo add category'''

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالاها'

