import tools
from tools import search_product, check_price


def test_search_existing_product():
    result = search_product.invoke({"query": "laptop"})

    assert "laptop" in result.lower()


def test_p002_price():
    result = check_price.invoke({"product_id": "P002"})

    assert "15000 RWF" in result


def test_unknown_product_price():
    result = check_price.invoke({"product_id": "P999"})

    assert "not found" in result.lower()


def test_tool_exception(monkeypatch):
    monkeypatch.setattr(tools, "products", None) 

    result = check_price.invoke({"product_id": "P002"})
    assert "unavailable" in result.lower()