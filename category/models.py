from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=250)
    slug = models.SlugField(_("عنوان"),max_length=50,null=True)
    created_at = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان به روز رسانی"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'