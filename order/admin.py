from django.contrib import admin
from .models import Ordering

# Register your models here.


class OrderingAdmin(admin.ModelAdmin):
    fields = ("user", ("product_names", "total_products"), "created_at", "updated_at")
    readonly_fields = ("updated_at", "created_at")
    list_display = (
        "user",
        "transaction_id",
        "created_at",
        "updated_at",
        "product_names",
        "total_products",
    )
    save_on_top = True

    # add 1 gift to list
    def add_gift(self, request, queryset):
        for req in queryset:
            req.total_products += 1
            req.save()
        self.message_user(request, "انجام شد")

    actions = ("add_gift",)


admin.site.register(Ordering, OrderingAdmin)
