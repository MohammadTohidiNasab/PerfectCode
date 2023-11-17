from django.db import models
from category.models import Category
from account.models import User
from django.utils.translation import gettext as _

# Create your models here.


# product model
class Product(models.Model):
    name = models.CharField(_("عنوان"), max_length=50, null=True)
    description = models.CharField(_("توضیحات"), max_length=250, null=True)
    price = models.CharField(_("قیمت"), max_length=50, null=True)
    stock = models.IntegerField(_("تعداد موجود"), default=0, null=True)
    color = models.CharField(_("رنگ"), max_length=50, null=True)
    is_active = models.BooleanField(_("فعال"), default=True, blank=True, null=True)
    image = models.ImageField(_("تصویر"), upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("زمان به روز رسانی"), auto_now=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ucomments")
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pcomments")
    reply = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="rcomments",
        blank=True,
        null=True,
    )
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.body[:30]}"

    class Meta:
        verbose_name = " نظر "
        verbose_name_plural = " نظرات "
