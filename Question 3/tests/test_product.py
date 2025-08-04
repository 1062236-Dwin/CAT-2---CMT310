import pytest
from ecommerce.product import Product

def test_create_valid_product():
    p = Product("Laptop", 1200.0, 10)
    assert p.name == "Laptop"
    assert p.price == 1200.0
    assert p.stock == 10

def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        Product("Phone", -500, 5)

def test_negative_stock_raises_error():
    with pytest.raises(ValueError):
        Product("Tablet", 300, -2)

def test_reduce_stock_successfully():
    p = Product("Mouse", 50, 10)
    p.reduce_stock(3)
    assert p.stock == 7

def test_reduce_stock_insufficient():
    p = Product("Keyboard", 70, 2)
    with pytest.raises(ValueError):
        p.reduce_stock(5)
