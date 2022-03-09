from django.urls import path
from .views import (HomeView, ItemDetailView, OrderSummaryView, 
                    CheckoutView, PaymentView, add_to_cart, remove_from_cart,
                    remove_single_item_from_cart)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view() , name='checkout'),
    path('order-summary/', OrderSummaryView.as_view() , name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view() , name='product'),
    path('add-to-card/<slug>/', add_to_cart , name='add-to-cart'),
    path('remove-from-card/<slug>/', remove_from_cart , name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, 
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view() , name='payment'),
]       