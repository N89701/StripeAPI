from django.urls import path

from .views import CreateCheckoutSessionView, get_stripe_config, ItemView

app_name = 'payments'

urlpatterns = [
    path(
        'buy/<int:item_id>/',
        CreateCheckoutSessionView.as_view(),
        name='buy_item'
    ),
    path('item/<int:item_id>/', ItemView.as_view(), name='item'),
    path('config/', get_stripe_config, name='config'),
]