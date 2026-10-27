import re

from langchain_core.tools import tool

from logging_config import get_logger
from products import products

logger = get_logger()




@tool
def search_product(query: str) -> str:
    """Search for a product by name or ID."""
    logger.info(f"event=tool_call tool=search_product input={query!r}")

    try:
        query = str(query).strip().lower()

        if len(query) < 2:
            logger.warning("event=tool_result tool=search_product outcome=invalid_input")
            return "Product not found."

        for product in products:
            if query in product["name"].lower() or query == product["id"].lower():
                logger.info(f"event=tool_result tool=search_product outcome=found id={product['id']}")
                return str(product)

        logger.info("event=tool_result tool=search_product outcome=not_found")
        return "Product not found."

    except Exception as error:
        logger.error( f"event=tool_failure tool=search_product error={error!r}", exc_info=True)
        return "Sorry, the product service is unavailable right now."


@tool
def check_price(product_id: str) -> str:
    """Check a product's price using its ID."""

    logger.info(f"event=tool_call tool=check_price input={product_id!r}")

    try:
        product_id = str(product_id).strip()

        for product in products:
            if product["id"].lower() == product_id.lower():
                logger.info(f"event=tool_result tool=check_price outcome=found id={product['id']}")
                return f'{product["name"]} costs {product["price"]} RWF.'

        logger.info(f"event=tool_result tool=check_price outcome=not_found input={product_id!r}")
        return "Product not found."

    except Exception as error:
        logger.error(
            f"event=tool_failure tool=check_price error={error!r}", exc_info=True
        )
        return "Sorry, the product service is unavailable right now."