import pytest
from ecommerce.product import Product
from ecommerce.cart import ShoppingCart
from ecommerce.order_processor import OrderProcessor

def test_place_order_reduces_stock():
    product = Product("Monitor", 100, 5)
    cart = ShoppingCart()
    cart.add_item(product, 3)

    processor = OrderProcessor()
    order_id = processor.place_order(cart)

    assert isinstance(order_id, str)
    assert product.stock == 2

def test_order_with_empty_cart_raises():
    cart = ShoppingCart()
    processor = OrderProcessor()
    with pytest.raises(ValueError):
        processor.place_order(cart)

def test_order_with_insufficient_stock_raises():
    product = Product("Hard Drive", 75, 2)
    cart = ShoppingCart()
    cart.add_item(product, 2)

    # Artificially reduce stock
    product.stock = 1

    processor = OrderProcessor()
    with pytest.raises(ValueError):
        processor.place_order(cart)
