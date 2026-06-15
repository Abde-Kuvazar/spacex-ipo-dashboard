def estimate_capital_flow(
    valuation,
    float_pct
):
    """
    Estimate passive ETF inflows (in billions USD)
    for a hypothetical SpaceX IPO.
    """

    public_cap = valuation * float_pct / 100

    passive_assets = 12000  # $12T passive assets

    sp500_market_cap = 55000  # $55T

    sp_weight = public_cap / (
        sp500_market_cap + public_cap
    )

    passive_inflow = passive_assets * sp_weight

    return passive_inflow