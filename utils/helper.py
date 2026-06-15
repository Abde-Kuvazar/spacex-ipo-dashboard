def format_market_cap(value):
    """
    Convert raw market cap to readable format.
    """

    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f} T"

    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f} B"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f} M"

    return str(value)