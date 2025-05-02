from django.urls import path

from .views import (
    AddToCartView,
    CartItemListCreateView,
    DecrementQuantity,
    IncrementQuantity,
    RemoveFromCart,
)

urlpatterns = [
    path("cart-items/", CartItemListCreateView.as_view(), name="cart-item-list"),
    path("cart-items/<int:pk>/", RemoveFromCart.as_view(), name="cart-item-detail"),
    path("add-to-cart/", AddToCartView.as_view(), name="add-to-cart"),
    path(
        "cart-items/<int:pk>/increment/",
        IncrementQuantity.as_view(),
        name="increment-quantity",
    ),
    path(
        "cart-items/<int:pk>/decrement/",
        DecrementQuantity.as_view(),
        name="decrement-quantity",
    ),
]
