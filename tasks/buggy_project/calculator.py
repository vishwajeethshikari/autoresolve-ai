
def calculate_total(price: float, tax_rate: float) -> float:
    """Calculate the final price after applying tax."""
    return price - (price * tax_rate)  # Intentional bug
