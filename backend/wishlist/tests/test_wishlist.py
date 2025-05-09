import pytest
from rest_framework import status
from django.urls import reverse
from products.models import Product
from wishlist.models import WishlistItem
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


# Fixtures
@pytest.fixture
def user():
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    return user


# @pytest.fixture
# def api_client(user):
#     client = APIClient()
#     client.login(username=user.username, password="testpassword")
#     return client


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


# Test Case: Create Wishlist Item
@pytest.mark.django_db
def test_create_wishlist_item(api_client, user):
    product = Product.objects.create(name="Test Product", price=10.0)

    url = reverse("wishlist-item-list-create")
    data = {"product": product.id}

    response = api_client.post(url, data=data)

    assert response.status_code == status.HTTP_201_CREATED

    assert WishlistItem.objects.filter(user=user, product=product).exists()


@pytest.mark.django_db
def test_create_wishlist_item_already_exists(api_client, user):
    product = Product.objects.create(name="Test Product", price=10.0)
    WishlistItem.objects.create(user=user, product=product)

    url = reverse("wishlist-item-list-create")
    data = {"product": product.id}

    response = api_client.post(url, data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["error"] == "Item already exists in wishlist"


@pytest.mark.django_db
def test_create_wishlist_item_missing_product(api_client):
    url = reverse("wishlist-item-list-create")
    data = {}  # No product ID

    response = api_client.post(url, data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["error"] == "productId is required"


# Test Case: Delete Wishlist Item
@pytest.mark.django_db
def test_delete_wishlist_item(api_client, user):
    product = Product.objects.create(name="Test Product", price=10.0)
    wishlist_item = WishlistItem.objects.create(user=user, product=product)

    url = reverse("wishlist-item-delete", kwargs={"pk": wishlist_item.id})

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    assert not WishlistItem.objects.filter(id=wishlist_item.id).exists()


# Test Case: Delete Wishlist Item Not Found
@pytest.mark.django_db
def test_delete_wishlist_item_not_found(api_client, user):
    url = reverse("wishlist-item-delete", kwargs={"pk": 99999})

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["error"] == "Not found."
