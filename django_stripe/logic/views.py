import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def get_stripe_config(request):
    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)
        domain = "http://127.0.0.1:8081"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    "price_data": {
                        "currency": item.currency,
                        "product_data": {"name": item.name},
                        "unit_amount": int(item.price * 100),
                    },
                    "quantity": 1,
                },
            ],
            mode='payment',
            success_url=f'{domain}/payment_success/',
            cancel_url=f'{domain}/payment_failed/',
        )
        return JsonResponse({'sessionId': checkout_session['id']})


class ItemView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        return render(request, 'item.html', {'item': item})
