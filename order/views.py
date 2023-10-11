from django.urls import reverse
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
import logging
from django.http import HttpResponse, Http404
from .models import Coupon, Ordering
from django.shortcuts import redirect
from .forms import CouponApplyForm
from django.contrib import messages
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 1000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = "+989112221234"  # اختیاری

    factory = bankfactories.BankFactory()
    bank = factory.create()
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url(reverse("callback-gateway"))
    bank.set_mobile_number(user_mobile_number)  # اختیاری

    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("&quotاین لینک معتبر نیست.&quot")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("&quotاین لینک معتبر نیست.&quot")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("&quotپرداخت با موفقیت انجام شد.&quot")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "&quotپرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت 48 ساعت پول به حساب شما بازخواهد گشت.&quot"
    )


class CouponApplyView(LoginRequiredMixin, View):
    form_class = CouponApplyForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                coupon = Coupon.objects.get(
                    code__exact=code,
                    valid_from__lte=now,
                    valid_to__gte=now,
                    active=True,
                )
            except Coupon.DoesNotExist:
                messages.error(request, "this coupon does not exists", "danger")
                return redirect("orders:order_detail", order_id)
            order = Ordering.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
        return redirect("orders:order_detail", order_id)
