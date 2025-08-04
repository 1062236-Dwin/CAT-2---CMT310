import pytest
from ecommerce.product import Product
from ecommerce.cart import ShoppingCart

@pytest.fixture
def product():
    return Product("Book", 20, 10)

def test_add_item_to_cart(product):
    cart = ShoppingCart()
    cart.add_item(product, 2)
    assert product in cart.items
    assert cart.items[product] == 2

def test_add_item_exceeding_stock_raises(product):
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(product, 20)

def test_add_invalid_quantity_raises(product):
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(product, 0)

def test_remove_item(product):
    cart = ShoppingCart()
    cart.add_item(product, 1)
    cart.remove_item(product)
    assert product not in cart.items

def test_calculate_total(product):
    cart = ShoppingCart()
    cart.add_item(product, 3)
    assert cart.calculate_total() == 60
